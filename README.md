# Sales data analysis - Marketplace

**The purpose of this analysis** is to optimize marketplace sales strategy to increase 1) revenue, 2) margins, and 3) customer retention.

The **tasks** include: 1) identification of key growth metrics, 2) optimization of the product range matrix (**ABC segmentation**), 3) analysis of the effectiveness of the pricing policy, 4) examination of customer behavior.

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

1) Dashboard on **sales** (["Online_Marketplace_Sales"](metabase/Metabase_Online_Marketplace_Sales.pdf)):
   - Daily / Weekly / Monthly revenue;
   - Total revenue;
   - Average discount;
   - Average Order Value (AOV);
   - Revenue and Number of Orders by Discount Size;
   - Weekly Revenue: Ratio to Median;
   - TOP-10 Products by Revenue;
   - TOP-10 Products by Average Order Value (AOV);
   - Monthly Sales Count;
   - Monthly Revenue Trend;
   - Average Order Value Trend

2) Dashboard on **customer behavior** (["Online_Marketplace_Customer_Behavior"](metabase/Metabase_Online_Marketplace_Customer_Behavior.pdf)):
   - Daily Active Users (DAU);
   - Weekly Active Users (WAU);
   - Monthly Active Users (MAU);
   - LTV;
   - Repeat Buyers (%);
   - Number of Customers;
   - Average Purchases per Customer;
   - Distribution of Purchases by Time of Day;
   - Rolling Retention

3) Dashboard on **product assortment** (["Online_Marketplace_Assortment"](metabase/Metabase_Online_Marketplace_Assortment.pdf)):
   - SKU Count;
   - Average List price;
   - Average Items per Order;
   - Distribution of Products (**ABC Segmentation**);
   - Combined ABC Segmentation;
   - TOP-10 Products with the highest units sold;
   - TOP-10 Products with the lowest units sold;
   - Monthly Sales Volume Trend;
   - Weekly Sales Volume: Ratio to Median;
   - Number of Orders per Month Decade;
   - Monthly Number of Orders
  
### 03 - Product Hypothesis Test Results

The file [product_hypothesis_test_results.py](python/product_hypothesis_test_results.py) documents the step-by-step process of hypothesis testing with applied statistical methods.

1) **Hypothesis 1**: on average, women spend more than men when shopping.

   **Result**: no significant difference in average order value (women vs. men). Customer gender does not influence average order value; men and women spend roughly the same.

3) **Hypothesis 2**: the average order size depends on the availability of a discount.

   **Result**: no significant difference in average items per order (no discount vs. discount). Discounts do not appear to impact how many items customers order on average (discount → no increase in average items per order). Order sizes remain nearly the same whether a discount is offered or not.

5) **Hypothesis 3**: the probability of placing an order is higher for discounted items compared to non-discounted items.

   **Result**: the null hypothesis is rejected; customers are overwhelmingly more likely to purchase discounted items (discounted items → purchased many times more than non-discounted).

7) **Hypothesis 4**: the average quantity of units sold decreases as product price increases.

   **Result**: no significant difference in average items per order (low vs. high-priced products). Product price does not appear to affect the average sales quantity in this dataset (high product price does not decrease the average sales volume). 

### 04 - Some Business Insights

1) Products X have high turnover but low average order value → consider testing bundling strategies.

2) The peak sales months are January, February, and November. Launch new items before peaks → test demand with limited batches.

3) Discounts are the primary driver of sales. Price & discount optimization: within the ABC segmentation framework, it is recommended to

   (1) limit discounts for Group B (mid-range) products to a maximum of 50% in order to preserve profitability;

   (2) implement discount promotions for Group C products before their phase-out.

   Implementation of these customer base strategies will help achieve: (1) higher product margins; (2) lower losses from over-discounting; (3) balanced pricing structure

5) Customer base strategy:

   (1) personalized email offers → 30/60/90 days post-purchase;

   (2) referral program;

   (3) loyalty system with cumulative discounts.

   Implementation of these customer base strategies will help achieve: (1) increased retention; (2) more repeat purchases & higher LTV; (3) DAU/WAU/MAU growth → stable order flow

For a detailed overview of the applied metrics, results of product hypothesis testing, and strategic recommendations, please refer to the full [report](report/Online_Marketplace_Report.pdf)
