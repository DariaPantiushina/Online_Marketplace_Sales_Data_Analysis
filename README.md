# Sales data analysis - Marketplace

**The purpose of this analysis** is to optimize marketplace sales strategy to increase 1) revenue, 2) margins, and 3) customer retention.

The **tasks** include: 1) identification of key growth metrics, 2) optimization of the product range matrix (ABC segmentation), 3) analysis of the effectiveness of the pricing policy, 4) examination of customer behavior.

## Data

1) sales(client_id, gender, purchase_datetime, purchase_time_seconds, product_id, quantity, price_per_item, discount_per_item, total_price):

**client_id** - customer ID (buyer);

**gender** - customer gender (F = Female, M = Male);

**purchase_datetime** - purchase date & time;

**purchase_time_seconds** - time of purchase in seconds since midnight;

**product_id** - unique product ID;

**quantity** - quantity of product units included in the purchase transaction;

**price_per_item** - unit price (pre-discount);

**discount_per_item** - discount per unit;

**total_price** - total cost of the purchase, computed as the product of the number of units purchased and the net unit price after applying discounts: (price_per_item – discount_per_item) × quantity

2) **Period** covered by the analysis: January 1, 2024 - December 31, 2024.

## Analysis: key steps and outcomes

### 01 - Configuring and establishing a process to import sales data from the marketplace using the API

- **Data_analytics** DB & **sales** table created
  
- The script [fetch_all_sales_data.py](python/fetch_all_sales_data.py) was developed to populate the database with all available historical sales data from the API (starting on 2024-01-01). It includes a mechanism to prevent re-downloading data for days that have already been retrieved

- The script [fetch_sales_data.py](python/fetch_sales_data.py) was set up to automatically retrieve the previous day’s sales data at 7 a.m. each day using the Windows Task Scheduler

- Logging is configured to the "log.txt" file

### 02 - Creating 3 dashboards in Metabase

- Established connection between Data_analytics database and Metabase

- Developed SQL queries to retrieve and display the following key metrics on the dashboard:

1) Dashboard on **sales** (["Online_Marketplace_Sales"](metabase/Metabase_Online_Marketplace_Sales.pdf), also available via public link: http://localhost:3000/public/dashboard/48405444-bb0f-4103-9a3a-816b4c8ba3a3): Daily / Weekly / Monthly revenue; Total revenue; Average discount, Average Order Value (AOV); Revenue and Number of Orders by Discount Size; TOP-10 Products by Revenue; TOP-10 Products by Average Order Value (AOV); Monthly Sales Count; Monthly Revenue Trend; Average Order Value Trend

2) Dashboard on **customer behavior** (["Online_Marketplace_Customer_Behavior"](metabase/Metabase_Online_Customer_Behavior.pdf), also available via public link: http://localhost:3000/public/dashboard/2c5560be-9e2d-463b-b756-3250f4b90551): Daily Active Users (DAU); Weekly Active Users (WAU); Monthly Active Users (MAU); LTV; Repeat Buyers (%); Number of Customers; Average Purchases per Customer; Distribution of Purchases by Time of Day; Rolling Retention
