from  dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector = embeddings.embed_query("Hello world")

print(vector)
print(len(vector))