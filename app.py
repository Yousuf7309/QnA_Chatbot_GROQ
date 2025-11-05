import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot with GROQ"
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

prompt = ChatPromptTemplate(
    [
        ("system","You're a good Q&A chatbot agent, Please response to the user queries, with a joyful tone. and you're name is jarvis greet the user first by introducing you a little."),
        ("user","Question:{question}")
    ]
)

def generate_response(question,llm,temperature,max_tokens):
    llm = ChatGroq(model=llm)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain.invoke({"question":question})
    return answer

#Title of the app
st.title("Simple Q&A Chatbot With Groq")

#Sidebar for settings
st.sidebar.title("Settings")

#Drop down to select various Open AI models
llm=st.sidebar.selectbox("Select Model from here:",["llama-3.3-70b-versatile", "llama-3.1-8b-instant"])

#Adjust response parameter
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens",min_value=50, max_value=300, value=150)

#Main interface for user input
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the query")