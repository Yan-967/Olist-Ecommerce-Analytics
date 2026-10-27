"""Read-only quality checks for the two CSV exports produced by the Olist notebook.

Run from the project root: python scripts/validate_exports.py
This script never modifies source or processed data.
"""

from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "processed"


def main():
    orders_path = DATA_DIR / "orders_dashboard.csv"
    items_path = DATA_DIR / "order_items_dashboard.csv"
    for p in (orders_path, items_path):
        if not p.is_file():
            print(f"ERROR: Missing {p}")
            print("Run the Jupyter notebook through the export-validation section first.")
            return 1

    orders = pd.read_csv(orders_path, encoding="utf-8-sig")
    items = pd.read_csv(items_path, encoding="utf-8-sig")
    checks = []

    def verify(label, ok, details):
        checks.append((label, bool(ok)))
        print(f"{'PASS' if ok else 'FAIL'} | {label}: {details}")

    verify("Orders shape", orders.shape == (96478, 15), str(orders.shape))
    verify("Items shape", items.shape == (110197, 7), str(items.shape))

    required_order_cols = {"order_id", "product_value", "freight_value", "items_total", "delivery_days", "is_late", "avg_review_score"}
    required_item_cols = {"order_id", "price", "freight_value"}
    if not required_order_cols.issubset(orders.columns) or not required_item_cols.issubset(items.columns):
        print("FAIL | Expected columns are missing; check the exported CSV schema.")
        return 1

    verify("No duplicate orders", orders["order_id"].is_unique, str(orders["order_id"].duplicated().sum()))
    verify("Items all reference known orders", items["order_id"].isin(orders["order_id"]).all(),
           str((~items["order_id"].isin(orders["order_id"])).sum()) + " unmatched item rows")

    products_from_orders = orders["product_value"].sum()
    products_from_items = items["price"].sum()
    verify("Cross-table product-value match", abs(products_from_orders - products_from_items) < 0.01,
           f"orders R$ {products_from_orders:,.2f} | items R$ {products_from_items:,.2f}")
    verify("Historical product-value check", abs(products_from_orders - 13221498.11) < 0.01,
           f"R$ {products_from_orders:,.2f}")
    verify("Historical freight-value check", abs(orders["freight_value"].sum() - 2198275.64) < 0.01,
           f"R$ {orders['freight_value'].sum():,.2f}")

    duration = pd.to_numeric(orders["delivery_days"], errors="coerce")
    late_bool = orders["is_late"].eq(True)
    verify("Valid durations", duration.notna().sum() == 96470, str(duration.notna().sum()))
    verify("Late deliveries", late_bool.sum() == 6534, str(late_bool.sum()))

    scores = pd.to_numeric(orders["avg_review_score"], errors="coerce").dropna()
    fractional_scores = ((scores % 1).abs() > 1e-10).sum()
    verify("Fractional review scores preserved", fractional_scores > 0,
           str(fractional_scores) + " non-integer order-level review scores")

    print("\nSummary: ", sum(ok for _, ok in checks), "/", len(checks), "checks passed", sep="")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    sys.exit(main())
