from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model

model= init_chat_model("openai/gpt-oss-120b", temperature=1, model_provider="groq", max_tokens=20)

response = model.invoke("poem on AI")

print(repr(response.content))