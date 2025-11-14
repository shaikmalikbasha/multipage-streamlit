# streamlit_app.py

import pymongo
import streamlit as st


# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    print("Function init_connection called")
    return pymongo.MongoClient(**st.secrets["mongo"])


client = init_connection()


# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data():
    db = client.costrategix
    items = db.employees.find()
    items = list(items)  # make hashable for st.cache_data
    return items


items = get_data()

# Print results.
st.metric(label="Total Employees", value=len(items))
