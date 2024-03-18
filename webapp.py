import streamlit as st
from functions import currency_converter

st.title("Currency Converter")
amount = st.text_input("Enter amount")
currency = st.radio("Select currency:", ["GBP to USD", "GBP to JPY", "USD to GBP", "JPY to GBP"])


if amount:
    try:
      new_amount = currency_converter(float(amount), currency)
      col1, col2 = st.columns([1, 2])
      with col1:
        st.text("Converted amount: ")
      with col2:
        st.text(new_amount)

    except ValueError:
        st.info("Amount must be a number")
