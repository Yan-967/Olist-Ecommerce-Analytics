# Power BI report: non-destructive structure review

**Source:** `powerbi/Olist_Ecommerce_Analytics.pbix` supplied by the project owner on October 26, 2026.  
**SHA-256:** `c687c8c2f3988b781f1f327b948292c335b75683fa333c54f811ad55ac4ca1ab`  
**Approximate file size:** 13,404,804 bytes.

## Verified by inspecting the saved PBIX package

The uploaded file is a valid, readable ZIP-based PBIX container: the ZIP integrity test passed, and a `DataModel` member was present. The following saved page definitions and visual counts were observed:

| Report page | Saved visuals | Visual composition |
|---|---:|---|
| Sales Overview | 7 | 3 cards, 1 line chart, 1 horizontal bar chart, 2 slicers |
| Logistics Performance | 8 | 4 cards, 3 horizontal bar charts, 1 slicer |
| Customer Satisfaction | 8 | 4 cards, 3 column charts, 1 slicer |

The report definitions reference `orders_dashboard`, `order_items_dashboard`, DAX measures and regional/date slicers, consistent with the source notebook's two exported datasets and the Power BI workflow described in this README.

## Validation boundaries

- **Verified:** File can be read without archive errors; three pages and their visual definitions exist; original bytes were preserved when packaged (hash compared before and after copying).
- **Previously confirmed with the project owner:** Displayed key KPIs and a corrected decimal review-score type; the notebook's four export validation outputs were provided in a screenshot.
- **Not validated here:** Power BI Desktop runtime rendering, all visual filter behavior, every DAX measure definition inside the binary tabular model, source refresh against a new machine's paths, or independent recalculation of aggregates against the raw nine CSV datasets.

## Final preparation in Power BI Desktop

1. Open the included PBIX and verify all three pages display properly.
2. Before refreshing, inspect **Transform data → Data source settings**. The saved report may reference CSVs in an earlier local Downloads path. If needed, point each source to the two CSVs generated in `data/processed/` and save a **copy** of the report.
3. Clear any temporary geographic or date filters before preparing screenshots.
4. **Completed by the project owner on October 26, 2026:** full-page report captures are stored in `screenshots/sales_overview.png`, `screenshots/logistics_performance.png`, and `screenshots/customer_satisfaction.png`.
5. **Completed:** The README embeds these images. The report can still be reopened in Power BI Desktop for further visual adjustments before publishing updates.

**Reproducibility note:** the report's embedded model and the processed CSV outputs are not interchangeable. The notebook's processed CSVs are generated in `data/processed/`; running the notebook does not silently change the saved PBIX or its query connections.

## Screenshot evidence – 26 Oct 2026

The owner supplied full-date-range images of the three report pages. Visible cards match these previously reported values:

| Page | Visible indicators |
|---|---|
| Sales | R$13.22 Mi product value, 96,478 orders, R$159.83 average order value |
| Logistics | 12.56-day average delivery time, 96,470 valid deliveries, 6,534 late, 6.77% late rate |
| Satisfaction | 4.29 on-time review score, 2.27 late review score, 9.23% on-time low-rating rate, 62.36% late low-rating rate |

The regional delay-rate chart shows nine states under the currently saved Top N and minimum-denominator filters. These screenshots support the dashboard's displayed values but do not independently validate a Power BI data refresh.
