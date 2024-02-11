## Q&A chatbot
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env

import streamlit as st
import os

# function to load openai model and get response
def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),temperature=0.5)
    response = llm(question)
    return response

# initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input = st.text_input("Input: ",key="input")
response = get_openai_response(input)

submit = st.button("Ask the question")
# if ask button is clicked
if submit:
    st.subheader("the response is")
    st.write(response)
