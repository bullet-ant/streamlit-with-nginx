import streamlit as st

from utils import create_dummy_dataframe

st.set_page_config(page_title="Home | Introduction to Streamlit", layout="wide")

st.title("Welcome to Introduction to Streamlit")

student_dict = {
    "Name": ["XYZ", "ABC", "PQR"],
    "Contact": ["111111", "222222", "333333"],
    "Class": [1, 1, 2],
}

dataframe = create_dummy_dataframe(student_dict)

st.dataframe(dataframe, hide_index=True, use_container_width=True)
