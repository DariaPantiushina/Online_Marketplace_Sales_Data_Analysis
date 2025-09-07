#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import psycopg2
import os
from datetime import datetime, timedelta


# In[2]:


# API setup
API_URL = "http://final-project.simulative.ru/data"

# date: yesterday
DATE = (datetime.now() - timedelta(days = 1)).strftime("%Y-%m-%d") 

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


# In[3]:


def log_message(message):
    """Function for logging to a file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {message}\n"

    print(log_entry.strip())
    with open(LOG_FILE, "a", encoding = "utf-8") as log:
        log.write(log_entry)


# In[4]:


def fetch_data():
    """API request function"""
    try:
        log_message("API data request")
        params = {"date": DATE}
        response = requests.get(API_URL, params = params, timeout = 10)
        
        if response.status_code == 200:
            data = response.json()
            log_message(f"Data successfully received. Number of records: {len(data)}")
            return data
        else:
            log_message(f"Error: request failed: {response.status_code}, {response.text}")
            return None
    except Exception as e:
        log_message(f"API request error: {e}")
        return None


# In[5]:


def save_to_db(sales_data):
    """PostgreSQL write function"""
    try:
        log_message("Data entry into the database")
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
        log_message(f"Data - successfully stored in the database. The total number of records is {count}")
    except Exception as e:
        log_message(f"DB write error: {e}")


# In[6]:


if __name__ == "__main__":
    log_message("Running the script")
    
    print("Running the script")  
    sales_data = fetch_data()

    if sales_data:
        print(f"Data example: {sales_data[:3]}") 
        save_to_db(sales_data)
    else:
        print("Data not received")
        log_message("Data not received")

