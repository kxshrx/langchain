from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Gemini model (lightweight flash version)
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite')

# Define a dynamic multi-turn chat prompt template
chat_template = ChatPromptTemplate(
    [
        ('system', 'you are a customer support agent'),  # System role definition
        MessagesPlaceholder(variable_name='chat_history'),  # Dynamic placeholder for message history
        ('human', '{query}')  # Human message with current query
    ]
)

# Load chat history from file
chat_history = []
with open('02-PROMPTS/history.txt') as f:
    for line in f:
        line = line.strip()
        # Identify and load human messages
        if line.startswith("Human:"):
            chat_history.append(HumanMessage(content=line.replace("Human:", "").strip()))
        # Identify and load AI messages
        elif line.startswith("AI:"):
            chat_history.append(AIMessage(content=line.replace("AI:", "").strip()))

# Start interactive chat loop
while True:
    query = input("You: ")
    if query == 'exit':
        break  # Exit loop on command

    # Create full prompt using history and current query
    full_prompt = chat_template.invoke({
        'chat_history': chat_history,
        'query': query
    })

    # Generate response from the model
    response = model.invoke(full_prompt.messages)
    print("AI: ", response.content)

    # Persist new interactions to the history file
    with open('02-PROMPTS/history.txt', 'a') as f:
        f.write(f"Human: {query}\n")
        f.write(f"AI: {response.content}\n")

    # Uncomment below lines to update in-memory history if needed
    chat_history.append(HumanMessage(content=query))
    chat_history.append(AIMessage(content=response.content))










# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite')

# #chat prompt template dynamic multi turn messages
# chat_template = ChatPromptTemplate(
#     [
#     ('system','you are a customer support agent'),
#     MessagesPlaceholder(variable_name='chat_history'),
#     ('human','{query}')
#     ]
# )


# # chat hsitory 
# chat_history = []
# with open('02-PROMPTS/history.txt') as f:
#     for line in f:
#         line = line.strip()
#         if line.startswith("Human:"):
#             chat_history.append(HumanMessage(content=line.replace("Human:", "").strip()))
#         elif line.startswith("AI:"):
#             chat_history.append(AIMessage(content=line.replace("AI:", "").strip()))


# while True:
#     query = input("You: ")
#     if query == 'exit':
#         break

#     full_prompt = chat_template.invoke({
#         'chat_history':chat_history,
#         'query':query
#     })

#     response = model.invoke(full_prompt.messages)
#     print("AI: ",response.content)

#     # chat_history.append(HumanMessage(content=query))
#     # chat_history.append(AIMessage(content=response.content))


#     with open('02-PROMPTS/history.txt', 'a') as f:
#         f.write(f"Human: {query}\n")
#         f.write(f"AI: {response.content}\n")
