# Notebook optimization notes

- Source: `Olist_Ecommerce_Analysis.ipynb` (98 cells; 61 code, 37 Markdown).
- Final: `Olist_Ecommerce_Analysis_Final.ipynb` (86 cells; 51 code, 35 Markdown).
- Removed redundant displays and diagnostics: an initial orders preview, repeated missing-delivery investigation, extra descriptive delivery-time output, repeated review exploratory details, duplicate order-item/payment inspection, preliminary difference check that used a > R$0.01 threshold, a duplicate monthly-growth chart, and duplicated category coverage printout.
- Consolidated lightweight checks for review duplicates and category coverage.
- Removed repeated `pandas`, `numpy`, `matplotlib`, `seaborn`, and `pathlib` imports after the first cell.
- Preserved all essential KPI calculations, row-level aggregations, joins, data cleaning and transformations, reconciliation in integer cents, and the two Power BI CSV export/validation cells.
- No transaction records were edited, regenerated or removed in this revision. The workbook itself contains code and saved historical output but not the nine CSV source datasets.
- Validation: Python syntax checked for every code cell; notebook format validated; core transformation/export code compared with the organized source. End-to-end data execution is pending the original Olist CSVs.
- The `.pbix` report was not modified.

## Portfolio review – 26 Oct 2026

- Kept **all 51 code cells in the same order** as the prior lean notebook. Only the input-path configuration cell was changed; business KPI, transformation, joins, categories, and both Power BI export/validation code blocks are byte-for-byte unchanged.
- Made source CSV discovery portable: `data/raw` takes priority, followed by the existing `~/Downloads/archive`, with an optional explicit custom folder.
- Updated outdated README/notebook wording after the project owner's successful local export validation screenshot.
- Added a separate, read-only `scripts/validate_exports.py` for repeatable checks on generated CSVs.
- Excluded raw CSVs, dashboard images, and PBIX from the package because those source artifacts have not been supplied here.
- Static checks: nbformat, Python AST syntax on all 51 code cells, source-code preservation comparison for 50 analytical cells, and project ZIP integrity.
- The project owner's original `Untitled.ipynb` and the previous lean notebook were retained separately in a backup ZIP; neither was edited.

## PBIX integration – 26 Oct 2026

- Added `powerbi/Olist_Ecommerce_Analytics.pbix`, copied byte-for-byte from the uploaded file. SHA-256: `c687c8c2f3988b781f1f327b948292c335b75683fa333c54f811ad55ac4ca1ab`.
- Inspected PBIX container integrity, page definitions and visual inventory; documented constraints in `POWER_BI_REVIEW.md`.
- Added the user's screenshot of a successful local four-line export validation to `reports/validation/`.
- Updated README to describe the now-included PBIX and remaining dashboard screenshots.
- Did not change either notebook, any CSV, any DAX measure, or any embedded report data.

## Dashboard screenshots and GitHub presentation – 26 Oct 2026

- Included three owner-supplied final report screenshots, covering sales, logistics and customer satisfaction.
- Embedded screenshots in the README with descriptive captions and concise business insights.
- Updated POWER_BI_REVIEW.md and validation-status language to reflect the new visual evidence.
- Preserved the supplied PBIX and notebook **byte-for-byte**; the three screenshots were copied without alteration.
- Raw source CSVs were not supplied and are not included in the public-ready archive.
