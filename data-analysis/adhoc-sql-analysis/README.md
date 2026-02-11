# Market.db Business Performance Report

**Role:** Data Analyst (Portfolio Project)\
**Stack:** SQLite • SQL • Python • Pandas • Matplotlib • Seaborn •
Jupyter

---

## Overview

This project is an ad-hoc business performance analysis using a
relational SQLite database (`Market.db`, Northwind-style schema).

![ERD Diagram](/data-analysis/adhoc-sql-analysis/images/Northwind_E-R_Diagram.png)  
<center> <b> ERD Diagram of Market.db Schema </center>

The objective was to simulate a real-world analyst workflow: interpret a
normalized ERD, construct SQL queries to answer business questions,
validate outputs, and communicate findings using data visualizations and
statistical analysis.

All insights in this project are supported by query outputs shown in the
notebook.

---

## Data Source & Schema

ERD file location: `images/Northwind_E-R_Diagram.png`

### Core Tables Used

-   **Customers** (`CustomerID`)
-   **Orders** (`OrderID`, `CustomerID`, `ShipperID`)
-   **OrderDetails** (`OrderID`, `ProductID`, `Quantity`)
-   **Products** (`ProductID`, `SupplierID`, `Price`)
-   **Suppliers** (`SupplierID`)
-   **Shippers** (`ShipperID`)

### Join Relationships

Customers (1) ──── (n) Orders\
Orders (1) ──── (n) OrderDetails\
Products (1) ──── (n) OrderDetails\
Suppliers (1) ──── (n) Products\
Shippers (1) ──── (n) Orders

---

## Data Dictionary (Fields Used in Analysis)

  Table          Column      Description
  -------------- ----------- --------------------------------
  Products       Price       Unit selling price (EUR)
  OrderDetails   Quantity    Units ordered per product line
  Orders         OrderDate   Date order was placed
  Customers      Country     Customer location
  Suppliers      Country     Supplier origin
  Orders         OrderID     Unique transaction identifier

---

## Analyst Query Standards (SOP)

-   **Revenue Definition:** `Revenue = Quantity * Price`
-   **Order Volume Metric:** Count of distinct `OrderID`
-   **Supplier Popularity Metric:** Count of distinct orders containing
    products from a supplier
-   **Inactive Customers:** Defined using `LEFT JOIN` where
    `OrderID IS NULL`
-   **Null Handling:** DISTINCT used where necessary to prevent
    double-counting

---

## Executive Summary

-   The United States leads in total customers (13) and total orders
    (29).
-   Strong positive correlation between customer and supplier count by
    country (*r = 0.69, p = 0.002*).
-   The U.S. also has the highest number of inactive customers (5).
-   Quantity ordered and revenue show strong positive correlation (*r =
    0.69, p \< 0.01*).
-   *Laughing Lumberjack Lager* generated the lowest quantity (5 units)
    and lowest revenue (€70).
-   *Plutzer Lebensmittelgroßmärkte AG* leads supplier order
    participation.

---

## Business Questions Answered

1.  Products priced under €10
2.  Supplier country concentration
3.  Customer country concentration
4.  Least popular products by quantity
5.  Least popular products by revenue
6.  Countries with the most orders
7.  Countries with inactive customers
8.  Most popular suppliers by order participation

Each section includes: - SQL query - Result preview - Visualization -
Evidence-based interpretation

---

## Strategic Recommendations

1.  Re-engage inactive U.S. customers through targeted campaigns.
2.  Investigate Brazil's supplier gap (high customers, zero suppliers).
3.  Evaluate underperforming SKUs for pricing or discontinuation review.
4.  Strengthen partnerships with high-performing suppliers.
5.  Explore price elasticity testing for low-volume products.

---

## Repository Structure

```diagram
market-db-performance-report/
├─ data/
│  ├─ Market.db
│  └─ erd/
│     └─ Northwind_E-R_Diagram.png
├─ notebooks/
│  └─ adhoc_report.ipynb
├─ src/
│  ├─ sql_queries.py
│  └─ db_utils.py
├─ outputs/
│  ├─ figures/
│  └─ tables/
└─ README.md
```

---

## Attribution

This project originated from a learning prompt during The Knowledge
House fellowship.\
All analysis logic, statistical testing, visualization design, and
reporting narrative were independently rebuilt and expanded as part of
my professional portfolio.
