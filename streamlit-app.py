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

def map_availability(value):
    if value == True:
        return 'In Stock'
    else:
        return 'Out of Stock'

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
        df = pd.DataFrame(data, columns=columns, index= None)
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


st.write('---')
df['AVAILABILITY'] = df['AVAILABILITY'].apply(map_availability)


col1, col2, col3 = st.columns(3)
with col1:
    # Create a pie chart for the distribution of ratings
    rating_counts = df['RATING'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%')
    ax.axis('equal')
    st.subheader('Rating Distribution')
    st.pyplot(fig)


with col2:
    # Create a pie chart for the distribution of ratings
    availability_counts  = df['AVAILABILITY'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(availability_counts , labels=availability_counts.index, autopct='%1.1f%%')
    ax.axis('equal')
    st.subheader('Availability Distribution')
    st.pyplot(fig)

with col3:
    average_rating = df['RATING'].mean()
    st.subheader("Average Rating")
    st.markdown(
        f"""
        <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px; background-color: #f0f0f0;">
            {average_rating}
        </div>
        """, 
        unsafe_allow_html=True
    )
    average_price = df['PRICE'].mean()
    st.subheader("Average Price")
    st.markdown(
        f"""
        <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px; background-color: #f0f0f0;">
            {average_price}
        </div>
        """, 
        unsafe_allow_html=True
    )
st.write('---')
rated_5_books = df[df['RATING'] == 5]
st.subheader('Books with Rating 5')
st.dataframe(rated_5_books[['TITLE', 'PRICE', 'RATING', 'AVAILABILITY']])
st.write('---')
top_10_expensive_books = df.nlargest(10, 'PRICE')
st.subheader('Top 10 Most Expensive Books')
st.dataframe(top_10_expensive_books[['TITLE', 'PRICE', 'RATING', 'AVAILABILITY']])