# Vendor-Performance-Analysis-and-Recommendation
This project provides a complete vendor performance analysis using sales, purchase, pricing, and freight data to evaluate profitability, stock turnover, and vendor contribution. The goal is to uncover strategic opportunities to improve pricing, reduce inventory costs, identify high/low performing vendors, and optimize business decisions.

# Project Objectives

- Identify top & bottom performing vendors
- Improve pricing efficiency & profit margin
- Optimize inventory turnover & reduce holding cost
 Evaluate freight cost impact
- Reduce vendor dependency risk
- Empower decision-making with BI reporting
- 
# Dataset Summary

- The project uses multiple raw datasets integrated through SQL + Python:

| Dataset                       | Purpose                                |
| ----------------------------- | -------------------------------------- |
| **sales.csv**                 | Sales revenue, quantity, tax & pricing |
| **purchases.csv**             | Purchase cost & volume                 |
| **purchase_prices.csv**       | Standard price & case size             |
| **vendor_invoice.csv**        | Freight charges per vendor             |
| **begin_inventory.csv**       | Starting stock valuation               |
| **end_inventory.csv**         | Ending stock valuation                 |
| **vendor_sales_summary.xlsx** | Final combined performance dataset     |

- Additional derived metrics include:
- Gross Profit
- Profit Margin %
- Freight Cost %
- Stock Turnover
- Sales-to-Purchase Ratio

# Data Cleaning & Preparation

- Ingested raw CSVs using automatic chunking (50k rows)
- Stored structured tables in SQLite database
- Merged sales, purchases, pricing & freight tables
- Removed whitespace, fixed types & handled null values
- Filtered invalid records (zero sales, zero revenue, negative margins)
- Computed KPIs for brand + vendor + store level

# Dashboard Features
- The Power BI dashboard includes:
 -  Vendor Contribution Distribution
   - Identify top revenue & purchase contributors
 - Profit Margin Analysis
   - Product and vendor-level margin performance
 - Inventory Turnover Heatmap
   -Highlight slow-moving, unsold & high-demand stock
- Pricing vs Sales Volume
 - Detect high-margin but low-sales opportunity brands
-Freight Impact
  - Measure freight cost effect on profitability
- SKU & Brand Drilldowns
  -Interactive brand → product → store exploration

# Key Insights

- Top 10 vendors contribute ~66% of purchase volume → dependency risk
- Bulk purchases lower unit cost by ~72% → pricing advantage
- $2.7M in unsold inventory → stock optimization needed
- 198 brands show high margins but low sales → marketing & pricing opportunity
- Some SKUs show negative profit → cost mismatch
- Weak correlation between purchase price & sales → price elasticity stable

# Performance & Key Results

This analysis delivered measurable, data-driven outcomes including:

## Financial Impact

Identified loss-generating brands with negative gross profit

Quantified freight cost exposure up to the SKU level

Showed margin gap between high vs low vendors (41.5% vs 31.2%)

Highlighted opportunities to improve bottom-line profitability

## Inventory Optimization

Exposed $2.71M idle inventory tied up in slow/unsold stock

Located SKUs with zero sales volume but significant purchase cost

Pinpointed turnover extremes ranging from 0 to 274x

## Vendor Strategy

Revealed heavy vendor dependency:
65.7% of purchases from only 10 vendors

Created ranking system to classify vendor performance

Flagged overspending risk due to concentrated sourcing

## Revenue Optimization

Found brands with high profitability potential but low demand

Identified pricing mismatches between purchase and sales rates

Supported targeted promotion strategy to lift volume

Overall, the project enabled clearer insight into profit drivers, cost risks, and growth opportunities.

# Tools & Skills Used
| Category        | Tools                         |
| --------------- | ----------------------------- |
| Data Processing | Python, Pandas                |
| Database        | SQLite, SQLAlchemy            |
| Dashboard       | Power BI                      |
| Analysis        | Jupyter Notebook              |
| Reporting       | PDF, Excel                    |
| Modeling        | SQL aggregation + custom KPIs |

- Additional skills demonstrated:
  - ETL pipeline development
  - Data engineering (chunk ingestion + DB design)
  - Profitability modeling
  - Business analytics & visualization
  - Inventory & vendor analysis
