
import streamlit as st

st.title("Simple Sales Dashboard")

st.write("View monthly sales and compare sales across four months.")

months = ["January", "February", "March", "April"]

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

selected_month = st.selectbox("Select Month:", months)

selected_sales = sales[selected_month]

st.write("Selected Month:", selected_month)
st.metric("Monthly Sales", selected_sales)

st.write("### Monthly Sales Bar Chart")

st.bar_chart(list(sales.values()))
