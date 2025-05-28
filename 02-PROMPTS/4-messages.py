from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite')

history =[
    SystemMessage(content="you are a fitness coach and you are supposed to give precise and short answers in about 50-80 words")
]

while True:
    user_input = input("You: ")
    history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        break
    response = model.invoke(history)
    history.append(AIMessage(content=response.content))
    print("Coach: ", response.content)

print(history)
