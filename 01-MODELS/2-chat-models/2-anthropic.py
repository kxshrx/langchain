from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='')

result = model.invoke('your question here brooo ')

print(result.content)