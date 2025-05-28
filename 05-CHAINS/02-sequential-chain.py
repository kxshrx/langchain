from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite')

# bulding paragraph summary to tweet

summarising_prompt = PromptTemplate(
    template='Summarize the following book paragraph into exactly 3 lines without changing its meaning or tone:\n\n{paragraph}',
    input_variables=['paragraph']
)

tweet_prompt = PromptTemplate(
    template='Convert the following summary into a professional tweet:\n\n{summary}',
    input_variables=['summary']
)

parser = StrOutputParser()

chain = summarising_prompt | model | parser | tweet_prompt | model | parser

response = chain.invoke({'paragraph':'When a retired detective receives a mysterious letter from a long-lost love, he’s pulled back into a decades-old unsolved case. What begins as a personal journey turns into a citywide hunt for a serial killer who was never caught.'})

print(response)

chain.get_graph().print_ascii()












# OUTPUT OF THE ABOVE CODE

# Retired detective haunted by a past love's letter is pulled back into a cold case. His personal quest to solve it quickly becomes a city-wide hunt for a serial killer who once slipped through the cracks. #Mystery #Thriller #ColdCase #Detective
#       +-------------+      
#       | PromptInput |      
#       +-------------+      
#              *             
#              *             
#              *             
#     +----------------+     
#     | PromptTemplate |     
#     +----------------+     
#              *             
#              *             
#              *             
# +------------------------+ 
# | ChatGoogleGenerativeAI | 
# +------------------------+ 
#              *             
#              *             
#              *             
#     +-----------------+    
#     | StrOutputParser |    
#     +-----------------+    
#              *             
#              *             
#              *             
# +-----------------------+  
# | StrOutputParserOutput |  
# +-----------------------+  
#              *             
#              *             
#              *             
#     +----------------+     
#     | PromptTemplate |     
#     +----------------+     
#              *             
#              *             
#              *             
# +------------------------+ 
# | ChatGoogleGenerativeAI | 
# +------------------------+ 
#              *             
#              *             
#              *             
#     +-----------------+    
#     | StrOutputParser |    
#     +-----------------+    
#              *             
#              *             
#              *             
# +-----------------------+  
# | StrOutputParserOutput |  
# +-----------------------+  