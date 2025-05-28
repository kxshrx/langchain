from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite')

st.title("Research Paper Summarizer")

user_input = st.text_input("Enter the name of your research paper")
length_input = st.number_input("Enter the preferred length of the summary (no of words)")
style_input = st.text_input("Enter the style or tone (eg: academic, simplified, formal, explanatory)")


# first way
#
# template = PromptTemplate(
#     template="""Summarize the research paper titled {user_input} in a {style_input} tone, with a length of approximately {length_input} words. The summary should cover the main objective of the study, the methodology or experimental setup, and highlight any important mathematical models, equations, or formulations, explaining them briefly where appropriate. It should also include the key results and findings, along with the conclusion or broader implications of the work. Ensure that both the technical and mathematical aspects are clearly conveyed in a way that aligns with the chosen tone and summary length.""",
#     input_variables=['user_input', 'style_input','length_input'],
#     validate_template=True
# )

template = load_prompt('research_query_template.json')


prompt = template.invoke({
    'user_input': user_input,
    'style_input':style_input,
    'length_input':length_input
})



if st.button("Summarise"):

    response = model.invoke(prompt)

    st.write(response.content)


