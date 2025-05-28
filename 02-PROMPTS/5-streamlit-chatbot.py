import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv
import os

# Load environment variables (e.g. Google API key)
load_dotenv()

# Set page config
st.set_page_config(page_title="Fitness Coach Chat", page_icon="💪")

# Title
st.title("💪 Ask Your Fitness Coach")

# Initialize the model
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite')

# Initialize chat history in session_state
if "history" not in st.session_state:
    st.session_state.history = [
        SystemMessage(content="you are a fitness coach and you are supposed to give precise and short answers in about 50-80 words")
    ]

# Text input
user_input = st.text_input("Ask a fitness question", placeholder="e.g. What's a good workout for fat loss?")

# Submit button
if st.button("Send") and user_input:
    st.session_state.history.append(HumanMessage(content=user_input))
    response = model.invoke(st.session_state.history)
    st.session_state.history.append(AIMessage(content=response.content))
    st.write(f"**Coach:** {response.content}")

# Show chat history (excluding the system prompt)
with st.expander("Chat History"):
    for msg in st.session_state.history[1:]:  # Skip system message
        if isinstance(msg, HumanMessage):
            st.markdown(f"**You:** {msg.content}")
        elif isinstance(msg, AIMessage):
            st.markdown(f"**Coach:** {msg.content}")
