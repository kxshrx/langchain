from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite')


# class Review(TypedDict):
#     summary : Annotated[str,'a breif summary of the user input in your won words']
#     sentiment : str

class Review(BaseModel):
    id : Optional[int] = Field(default=None, description='the id of the reviewer')
    user : str = Field(default='Anonymous', description='the name ofthe reviewer')
    keythemes : list[str] = Field(description='write down all the key themse decribed in review in list')
    summary : str = Field(description='it is the concise and true summary of the review but in a cirsp and shortened way represented in shortened bulletins')
    sentiment : Literal['positive', 'negative', 'netural'] = Field(description='it could be either positive , negative or a neutral review')
    pros : Optional[str] = Field(default=None, description="the positives mentioned in the review ")
    cons : Optional[str] = Field(default=None, description="the negatives mentioned in the review ")



struct_model = model.with_structured_output(Review)


reviews = [
    "I am Kishore (userid = 3567830), recently bought this product and was genuinely impressed. The customer support was incredibly responsive, and my order arrived two days early. The interface is intuitive, even for someone like me who's not very tech-savvy. I'd say the key themes are great support, fast delivery, and user-friendly design. Overall, I’m very happy with the experience. Pros: quick assistance, early delivery, and an easy-to-use layout. Honestly, there were no major cons I could find. Definitely a positive review.",

    "The product works as expected, but there's nothing exceptional about it. The performance is average, and while the battery lasts a decent amount of time, I’ve noticed a lack of software updates which is concerning. I'd classify this as a neutral experience. The key themes here are average performance, okay battery life, and minimal ongoing support. I’m not unhappy, but I wouldn’t rave about it either.",

    "The build quality is really disappointing. Within a week of use, the device started showing issues. It’s clearly overpriced for the features it offers, and to make matters worse, customer service was completely unresponsive. From my perspective, the key themes would be poor durability, unjustified cost, and bad service. Overall, a negative experience. Cons: weak build, expensive for its value, no help when I reached out."
]


for review in reviews:
    response = struct_model.invoke(review)
    # print(response)
    with open("03-STRUCT-OUTPUT/review_output.txt", "a") as file:
        file.write(response.model_dump_json()+"\n\n\n\n")

    print("*-*-*-*-*-"*25)

