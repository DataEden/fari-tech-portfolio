# Market.db Business Performance Report

**Fari Lindo • DataInsideData™**

**Role:** Data Analyst (Portfolio Project)

---

## Overview

This project is an ad-hoc business performance analysis using a
relational SQLite database (`Market.db`, Northwind-style schema).

![ERD Diagram](images/Northwind_E-R_Diagram.png)

**<center>ERD Diagram of Market.db Schema</center>**

The objective was to simulate a real-world analyst workflow:

- Interpret a normalized ERD, construct SQL queries to answer business questions,
validate outputs, and communicate findings using data visualizations and
statistical analysis.

> *All insights are supported by query outputs generated and found in the [project notebook](/data-analysis/dhoc-sql-analysis/notebooks/adhoc_report.ipynb)*.

## Executive Summary

- The United States is the dominant demand market, leading in total customers (13) and total orders (29). However, it also has the highest number of inactive customers (5), highlighting a clear re-engagement opportunity.

- Customer concentration and supplier presence are positively aligned by country (r = 0.69, p = 0.002), suggesting markets with higher demand tend to attract greater supplier participation. Notably, Brazil exhibits strong customer demand (9) but zero suppliers, indicating potential reliance on imports.

- Revenue performance is primarily volume-driven. A strong positive relationship exists between quantity ordered and total revenue (r = 0.69, p < 0.01), indicating that increasing sales volume is a key revenue lever.

- Product underperformance identified: Laughing Lumberjack Lager generated both the lowest quantity (5 units) and lowest total revenue (€70), suggesting pricing, positioning, or demand issues.

- Supplier participation is concentrated. Plutzer Lebensmittelgroßmärkte AG leads in order coverage (42 distinct orders), indicating both strategic importance and potential supplier dependency risk.

- Inactive customer patterns scale with market size. While countries with more orders tend to have more inactive customers (r = 0.49), the relationship is not statistically significant (p > 0.05), suggesting engagement gaps may vary by market maturity.

## 📊 Visual Highlights

**Figure 1: Inactive Customers by Country**

![Inactive Customers by Country](images/countries-with-no-orders-by-number-of-customers.png)

*<center>Distribution of customers with zero orders across countries.</center>*

---

**Figure 2: Relationship Between Total Orders and Inactive Customers by Country (r = 0.49, p = 0.10)**

![Correlation Between Total Orders and Inactive Customers by Country](images/corr-bet-most-orders-and-no-orders-by-country.png)

*<center>Country-level scatter plot showing the relationship between total orders and customers with no orders. A moderate positive relationship is observed (r = 0.49), though not statistically significant (p > 0.05).</center>*

---

**Figure 3: Relationship Between Total Quantity Ordered and Total Revenue by Product (r = 0.69, p < 0.01)**

![Quantity vs Revenue](images/correlation-quantity-vs-revenue.png)

*<center>Product-level scatter plot showing a strong positive relationship between quantity ordered and total revenue. Revenue performance is primarily volume-driven.</center>*

---

**Figure 4: Supplier Distribution by Country**

![Suppliers by Country](images/number-of-suppliers-by-country.png)

*<center>Distribution of suppliers by country. The United States, Germany, and France have the highest supplier presence, aligning with customer concentration patterns.</center>*

## Data Source & Schema

**ERD file location:** `images/Northwind_E-R_Diagram.png`

### Core Tables Used

- **Customers** (`CustomerID`)
- **Orders** (`OrderID`, `CustomerID`, `ShipperID`)
- **OrderDetails** (`OrderID`, `ProductID`, `Quantity`)
- **Products** (`ProductID`, `SupplierID`, `Price`)
- **Suppliers** (`SupplierID`)
- **Shippers** (`ShipperID`)

### Join Relationships

    Customers (1) ──── (n) Orders
    Orders (1) ──── (n) OrderDetails
    Products (1) ──── (n) OrderDetails
    Suppliers (1) ──── (n) Products
    Shippers (1) ──── (n) Orders

---

## <center>Data Dictionary (Fields Used in Analysis)</center>

| Table        | Column     | Description                     |
|--------------|------------|---------------------------------|
| Products     | Price      | Unit selling price (EUR)        |
| OrderDetails | Quantity   | Units ordered per product line  |
| Orders       | OrderDate  | Date order was placed           |
| Customers    | Country    | Customer location               |
| Suppliers    | Country    | Supplier origin                 |
| Orders       | OrderID    | Unique transaction identifier   |

---

## Analyst Query Standards (SOP)

To ensure consistency and reproducibility:

- **Revenue Definition:** `Revenue = Quantity * Price`
- **Order Volume Metric:** Count of distinct `OrderID`
- **Supplier Popularity Metric:** Count of distinct orders containing
    products from a supplier
- **Inactive Customers:** Defined using `LEFT JOIN` where
    `OrderID IS NULL`
- **Null Handling:** Verified joins to prevent double-counting;
    `DISTINCT` used when aggregating across multi-line joins

---

## Business Questions Answered

This analysis addresses 8 core business questions:

1. Products priced under €10
2. Supplier country concentration
3. Customer country concentration
4. Least popular products by quantity
5. Least popular products by revenue
6. Countries with the most orders
7. Countries with inactive customers
8. Most popular suppliers by order participation

Each section includes:

- SQL query
- Result preview
- Visualization
- Evidence-based interpretation

---

## Strategic Recommendations

1. Re-engage inactive U.S. customers via targeted campaigns.
2. Investigate Brazil's supplier gap (high customers, zero suppliers).
3. Evaluate underperforming SKUs for pricing or discontinuation review.
4. Strengthen partnerships with high-performing suppliers.
5. Explore price elasticity testing for low-volume products.

---

## Repository Structure

    adhoc-sql-analysis/
    ├─ db/
    │  └─ Market.db
    ├─ images/
    │  └─ Northwind_E-R_Diagram.png
    |  └─ countries-with-no-orders-by-number-of-customers.png
    |  └─ corr-bet-most-orders-and-no-orders-by-country.png
    |  └─ correlation-quantity-vs-revenue.png
    |  └─ number-of-suppliers-by-country.png
    ├─ notebooks/
    │  └─ Northwind_E-R_a_dhoc_report.ipynb
    ├─ README.md
---

## How to Run

### Option A --- Jupyter Notebook

```bash
pip install -r requirements.txt
jupyter lab
```

Open:

    adhoc_report.ipynb

### Option B --- VS Code SQLite Viewer

Install the SQLite extension and open:

    db/Market.db

You may also test queries in the terminal using:

``` bash
sqlite3 db/Market.db
```

---

## Key Skills Demonstrated

- Relational schema interpretation from ERD
- Multi-table joins across normalized structure
- Aggregations and grouped analysis
- Correlation analysis (Pearson r, p-values)
- Evidence-based business storytelling
- Clean, modular SQL and Python workflow

---

## Attribution

This project originated from a learning prompt during The Knowledge
House fellowship.\
All analysis logic, statistical testing, visualization design, and
reporting narrative were independently rebuilt and expanded as part of
my professional portfolio.

---

## Future Enhancements

- Extend analysis to time-series revenue trends
- Implement window functions for ranking
- Deploy as an interactive dashboard (Streamlit)

## Contact

### Fari Lindo • DataInsideData™

- [GitHub](https://github.com/dataeden)
- [Portfolio](https://datainsidedata.com)
- [LinkedIn](https://www.linkedin.com/in/fari-lindo/)  
- [Email](mailto:contact@datainsidedata.com)

*Tech Hands, a Science Mind, and a Heart for Community™*