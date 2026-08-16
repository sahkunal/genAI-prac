from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import Optional, List
from langchain_core.output_parsers import PydanticOutputParser


# 1. Create the model
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0
)

class Movie(BaseModel):
    title: Optional[str]
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    main_cast: List[str]
    duration: List[str]

parser = PydanticOutputParser(pydantic_object=Movie)


# 2. Create the prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """Extract the following information from the movie description provided by the user.{format_instructions}"""
    ),
    (
        "human",
        "{movie_description}"
    )
])

para= input("Enter your prompt: ")
final_prompt= prompt.invoke({
    "movie_description": para,
    'format_instructions': parser.get_format_instructions()
})
response = model.invoke(final_prompt)

# 6. Print the result
print(response.content)