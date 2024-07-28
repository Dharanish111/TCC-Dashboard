import streamlit as st
import pandas as pd
from appwrite.client import Client
from appwrite.services.databases import Databases

# Initialize the Appwrite client
client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1')
client.set_project('66a0f45300119ac4db4b')
client.set_key('40ae0b07bc54a6128dcb36dde09e2f8c3b4ce7c43f222a2348ac3c63ae5e2eb2f9ea8f5f758881c3913fe8fe3d34c25c0e4ed949b38ba867e57eb5c81611070ac561f2f1f9cee10baf329473b17f6819ec535ac1cf8b2eca5317a2c4cb7b2d4cdfabb204402cdc5df4126285ff712cb34a78a58f405db119f24465b04fd1e520')

databases = Databases(client)

def get_data_from_appwrite(database_id, collection_id):
    documents = databases.list_documents(database_id, collection_id)
    return documents['documents']

# Replace with your actual database ID and collection ID
database_id = "66a0f79f058c0e730bc3"  # You need to specify the database ID here
collection_id = "66a0f7a04b4e3af9272c"  # You need to specify the collection ID here

data = get_data_from_appwrite(database_id, collection_id)

if data:
    # Process and display data
    df = pd.json_normalize(data)  # Normalize JSON data for better visualization
    st.write(df)
else:
    st.write("No data found in the collection.")
