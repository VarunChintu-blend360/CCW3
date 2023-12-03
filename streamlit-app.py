import streamlit as st

import snowflake.connector

# Snowflake connection parameters
account = 'vniqwci-jj28244'
user = 'varun'
password = 'Blend360'
warehouse = 'CCW3_WH'
database = 'CCW3_DB'

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


# set page configarations
st.set_page_config(page_title="Coding Challenge 3",layout="wide")

# Header section
st.header("Coding Challenge 3")
st.subheader("Varun Rao Chintu")

