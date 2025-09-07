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

### 01 - Establish a process to import sales data from the marketplace using the API

- **Data_analytics** DB & **sales** table created
  
- The script [fetch_all_sales_data.py](python/fetch_all_sales_data.py) was developed to populate the database with all available historical sales data from the API (starting on 2024-01-01). The script includes a mechanism to prevent re-downloading data for days that have already been retrieved.
