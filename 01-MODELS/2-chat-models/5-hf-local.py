from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from dotenv import load_dotenv
import os



load_dotenv()
hf_token = os.getenv("HUGGINGFACE_API_TOKEN")

print(f"Token found: {'Yes' if hf_token else 'No'}")
if hf_token:
    print(f"Token starts with: {hf_token[:10]}...")


# Download and load DialoGPT-small (400MB download)
model_id = "microsoft/DialoGPT-small"
print("Downloading DialoGPT-small model...")

tokenizer = AutoTokenizer.from_pretrained(model_id, token=hf_token)
model = AutoModelForCausalLM.from_pretrained(model_id, token=hf_token)

print("Model downloaded!")

# Create simple pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    # max_new_tokens=50
)

# Wrap with LangChain ChatHuggingFace (this model supports chat)
llm = HuggingFacePipeline(pipeline=pipe)
chat_model = ChatHuggingFace(llm=llm, model_id=model_id)

# Use it with your prompt
prompt = "yes give me a pizza recipe?"
result = chat_model.invoke(prompt)


print(result.content)
