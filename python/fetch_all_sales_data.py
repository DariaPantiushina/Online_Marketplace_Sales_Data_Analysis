#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import psycopg2
import os
from datetime import datetime, timedelta


# In[ ]:


# API setup
API_URL = "http://final-project.simulative.ru/data"

# DB setup
DB_CONFIG = {
    "dbname": "Data_analytics",
    "user": "postgres",
    "password": "1234",
    "host": "127.0.0.1",
    "port": "5432"
}

# path to log file
LOG_DIR = r"D:\Project"
LOG_FILE = os.path.join(LOG_DIR, "log.txt")


# In[ ]:


def log_message(message):
    """Function for logging to a file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {message}\n"

    print(log_entry.strip())  
    with open(LOG_FILE, "a", encoding = "utf-8") as log:
        log.write(log_entry)


# In[ ]:


def fetch_data(date):
    """API request function (by date)"""
    try:
        log_message(f"Request by {date}")
        response = requests.get(API_URL, params = {"date": date}, timeout = 10)

        if response.status_code == 200:
            data = response.json()
            log_message(f"Data loaded for {date} successfully received. Number of records: {len(data)}")
            return data
        else:
            log_message(f"Error: request failed ({date}): {response.status_code}, {response.text}")
            return None
    except Exception as e:
        log_message(f"Data fetch error ({date}): {e}")
        return None


# In[ ]:


def save_to_db(sales_data, date):
    """PostgreSQL write function"""
    try:
        log_message(f"Data for {date} is being recorded in the database")
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        insert_query = """
        INSERT INTO sales (client_id, gender, purchase_datetime, purchase_time_seconds, 
                           product_id, quantity, price_per_item, discount_per_item) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """

        count = 0
        for sale in sales_data:
            cur.execute(insert_query, (
                sale['client_id'],
                sale['gender'],
                sale['purchase_datetime'],
                sale['purchase_time_as_seconds_from_midnight'],
                sale['product_id'],
                sale['quantity'],
                sale['price_per_item'],
                sale['discount_per_item']
            ))
            count += 1

        conn.commit()
        cur.close()
        conn.close()
        log_message(f"Data for {date} - successfully stored in the database. The total number of records is {count}")
    except Exception as e:
        log_message(f"DB write error ({date}): {e}")


# In[ ]:


def get_existing_dates():
    """Get list of loaded dates from DB"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        cur.execute("SELECT DISTINCT purchase_datetime FROM sales;")
        existing_dates = {row[0].strftime("%Y-%m-%d") for row in cur.fetchall()}

        cur.close()
        conn.close()
        return existing_dates
    except Exception as e:
        log_message(f"Failed to fetch uploaded dates: {e}")
        return set()


# In[ ]:


if __name__ == "__main__":
    log_message("Begin full data download")

    # set date range
    start_date = datetime(2024, 1, 1)
    end_date = datetime.now() - timedelta(days = 1)  # up to yesterday

    existing_dates = get_existing_dates()  # fetch loaded dates

    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")

        if date_str in existing_dates:
            log_message(f"Skip {date_str} as it has already been loaded")
        else:
            sales_data = fetch_data(date_str)
            if sales_data:
                save_to_db(sales_data, date_str)

        current_date += timedelta(days = 1)

    log_message("All data downloaded")

