from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "pizza is my favourite dish"

vector = embedding.embed_query(text)

print(str(vector))

# import os
# os.environ.pop("HUGGINGFACEHUB_API_TOKEN", None)


# from sentence_transformers import SentenceTransformer
# sentences = ["pizza is my favourite dish", "Each sentence is converted"]

# model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
# embeddings = model.encode(sentences)
# print(embeddings)