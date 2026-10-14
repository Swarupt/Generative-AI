
import streamlit as st

st.title("Price Calculator")

price = st.number_input(
    "Enter product price:",
    min_value=0.0,
    value=1000.0
)

discount = st.slider(
    "Select discount percentage:",
    min_value=0,
    max_value=50,
    value=10
)

if st.button("Calculate Price"):
    discount_amount = price * discount / 100
    final_price = price - discount_amount

    st.success("Final Price: " + str(round(final_price, 2)))

    table_data = [
        ["Before Discount", price],
        ["Discount", str(discount) + "%"],
        ["After Discount", round(final_price, 2)]
    ]

    st.table(table_data)
