from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite')

prompt = PromptTemplate(
    template='give me 3 famous personalities who celebrate the birthday on this date (just names) {date}',
    input_variables=['date']
)

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({'date':'5 January'})

print(response)

chain.get_graph().print_ascii()