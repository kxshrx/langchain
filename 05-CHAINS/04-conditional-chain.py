from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite')

parser = StrOutputParser()

class Feedback(BaseModel):

    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))

chain.get_graph().print_ascii()



# Okay, here are a few options for responding to positive feedback, ranging in formality and depending on the context:

# **General & Versatile Responses:**

# *   "Thank you! I'm so glad you enjoyed it." (Simple, friendly, and works well in most situations)
# *   "I really appreciate you taking the time to let me know. It means a lot!" (Acknowledges the effort of the feedback giver)
# *   "That's wonderful to hear! Thank you for your kind words." (Enthusiastic and grateful)
# *   "I'm happy to hear that you had a positive experience. Thanks for the feedback!" (Focuses on the recipient's positive experience and thanks the giver)

# **More Specific Responses (Consider the context):**

# *   **If the feedback is about a product or service:** "Thank you! We're always striving to provide the best possible experience." (Highlights the company/individual's commitment to quality)
# *   **If the feedback is about a specific task or project:** "I'm thrilled you're happy with the results! I put a lot of effort into it." (Shows personal investment and acknowledges the work)
# *   **If the feedback is about your skills or abilities:** "Thank you! I appreciate the positive feedback. I'm always working to improve." (Humble and shows a desire for growth)
# *   **If the feedback came after a specific interaction:** "I'm so glad I could help! Please let me know if you need anything else." (Offers further assistance)
# *   **If the feedback is from a supervisor or manager:** "Thank you for your feedback. I'm glad to hear that my work is meeting expectations." (Professional and demonstrates awareness of expectations)

# **Tips for Choosing the Best Response:**

# *   **Consider the relationship:** Are you speaking to a friend, a colleague, a client, or a supervisor?
# *   **Consider the context:** What was the feedback about? What was the situation?
# *   **Be genuine:** Your response should reflect your true feelings.
# *   **Keep it concise:** Avoid rambling.
# *   **Personalize it (if possible):** If you know the person well, you can add a more personal touch.

# **Example Scenario:**

# **Feedback:** "That presentation was fantastic! You really captured everyone's attention."

# **Good Responses:**

# *   "Thank you so much! I'm glad you enjoyed it."
# *   "I really appreciate you saying that. I put a lot of work into it!"
# *   "That's wonderful to hear! Thanks for the feedback."

# **In short, the best response is one that is sincere, appropriate for the situation, and expresses your gratitude.**
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
#  +----------------------+  
#  | PydanticOutputParser |  
#  +----------------------+  
#              *             
#              *             
#              *             
#         +--------+         
#         | Branch |         
#         +--------+         
#              *             
#              *             
#              *             
#      +--------------+      
#      | BranchOutput |      
#      +--------------+      