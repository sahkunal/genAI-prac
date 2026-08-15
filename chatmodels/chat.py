from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model

model= init_chat_model("llama-3.3-70b-versatile", temperature=1, model_provider="groq")

response = model.invoke("poem on AI")

print(response.content)