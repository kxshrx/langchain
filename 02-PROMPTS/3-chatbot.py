from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite')

print("custom chatbot")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("AI: Bye")
        break

    response = model.invoke(user_input)
    print("AI: ",response.content)
    print("===================================")