import streamlit as st
from query_engine import process_query
from dotenv import load_dotenv

#Loading the environment variables
load_dotenv()

#Streamlit for interface
st.title("Data Analysis with Gemini")
st.write("Upload the datasets and ask queries about it")

#File uploading
uploaded_file1 = st.file_uploader("Upload Dataset 1", type="csv")
uploaded_file2 = st.file_uploader("Upload Dataset 2", type="csv")

if uploaded_file1 and uploaded_file2:
    query = st.text_input("Enter your queries")
    if st.button("Get Response"):
        with st.spinner("Analyzing and getting a response..."):
            analysis = process_query(query, uploaded_file1, uploaded_file2)
            st.write("Response from llm:")
            st.write(analysis)