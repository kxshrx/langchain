

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

# Load environment variables (e.g., API keys)
load_dotenv()

# Initialize the Gemini model
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite')

# Streamlit UI layout
st.title("🤖 Gemini Chatbot")
st.subheader("A simple chatbot using LangChain and Gemini")

# User input field
user_input = st.text_input("Ask me anything:")

# Handle the button click
if st.button('Get Answer'):
    if user_input.strip():
        response = model.invoke(user_input)
        st.markdown("**Response:**")
        st.write(response.content)
    else:
        st.warning("Please enter a question or message.")




# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# import streamlit as st

# load_dotenv()

# model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite')

# st.subheader("first langchain tryout")
# st.title("CHATBOT")
# user_input = st.text_input("Enter your text")
# if st.button('Answer'):
#     response = model.invoke(user_input)
#     st.write(response.content)
