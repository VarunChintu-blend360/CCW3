#!pip install snowflake-connector-python

import streamlit as st
import pandas as pd
import snowflake.connector
import matplotlib.pyplot as plt


# Snowflake connection parameters
account = 'vniqwci-jj28244'
user = 'varun'
password = 'Blend360'
warehouse = 'CCW3_WH'
database = 'CCW3_DB'
table_name = 'books_table'

def fetch_data_from_snowflake():
    try:
        # Snowflake connection
        conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account
        )
        # Snowflake cursor
        cur = conn.cursor()
        # Use the warehouse
        cur.execute(f"USE WAREHOUSE {warehouse}")

        # Use the database
        cur.execute(f"USE DATABASE {database}")
        cur.execute(f"SELECT Title, Price, Rating, Availability FROM {table_name}")
        data = cur.fetchall()
        columns = [x[0] for x in cur.description]
        df = pd.DataFrame(data, columns=columns)
        return df
    except Exception as e:
        st.error(f"Error fetching data: {e}")
    finally:
        conn.close()
df = fetch_data_from_snowflake()

# set page configarations
st.set_page_config(page_title="Coding Challenge 3",layout="wide")

st.title('Coding Challenge 3')
st.subheader("Varun Rao Chintu")


st.write('Data from Snowflake:')
st.dataframe(df)

