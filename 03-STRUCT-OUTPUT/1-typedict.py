# from typing import TypedDict

# class Person(TypedDict):
#     name : str
#     age: int

# new_person : Person= {'name':'Kishore', 'age':19}

# print(new_person)



from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite')


class Review(TypedDict):
    summary : Annotated[str,'a breif summary of the user input in your won words']
    sentiment : str

struct_model = model.with_structured_output(Review)

query = "The 2025 IPL season concluded with a thrilling final, as the Rajasthan Royals emerged victorious, claiming their second title after a long wait. The team's consistent performance throughout the tournament, backed by strong leadership and a blend of young talent and experienced players, proved to be the winning formula. Fans were especially thrilled by the standout performances from key players in both batting and bowling departments. The final match kept everyone on the edge of their seats, and this victory has now cemented the Royals’ legacy as one of the most resilient teams in IPL history."

response1 = model.invoke(query)
response2 = struct_model.invoke(query)

print(response1.content)
print("==============")
print(response2)


# LangChain (and the Google Generative AI wrapper) does NOT support TypedDict for structured output.