
import os
from dotenv import load_dotenv

load_dotenv()
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    
    pipeline_kwargs=dict(
        max_new_tokens=100,
        do_sample= False,
        repetition_penalty=1.2,
)
)
chat_model= ChatHuggingFace(llm= llm)

result =chat_model.invoke("what is hugging face and local model?")

print(result.content)