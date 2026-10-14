
import streamlit as st

st.title("Product Form")

st.sidebar.header("Enter Product Details")

name = st.sidebar.text_input("Product Name")

category = st.sidebar.selectbox(
    "Select Category:",
    ["Electronics", "Clothing", "Food", "Books", "Accessories"]
)

price = st.sidebar.number_input(
    "Enter Price:",
    min_value=0.0,
    value=100.0
)

if st.sidebar.button("Add Product"):

    if name.strip() == "":
        st.error("Please enter a product name.")

    else:
        st.success("Product added successfully!")

        st.write("### Product Details")
        st.write("Product Name:", name)
        st.write("Category:", category)
        st.write("Price:", price)
