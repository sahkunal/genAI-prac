from dotenv import load_dotenv load_dotenv() from langchain_mistralai import ChatMistralAI from langchain_core.prompts import ChatPromptTemplate


# 1. Create the model
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0
)

# 2. Create the prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a movie information extraction assistant.

Your job is to take a long movie description and reduce it to
only the important information.

Do NOT invent information that is not present in the input.

Extract:
- Movie title
- Release year
- Genre
- Director
- Main cast
- Duration
- Language
- Country
- Rating
- Main characters
- Themes
- Likes
- Dislikes
- Overall opinion

Also create a short summary of the movie in 2-3 sentences.

If some information is not available, write "Not mentioned".

Keep the response concise."""
    ),
    (
        "human",
        "{movie_description}"
    )
])


# 3. Connect prompt + model
chain = prompt | model

# 5. Send the movie description to the model
response = chain.invoke({
    "movie_description": movie_description
})
para= input("Enter your prompt: ")
final_prompt= prompt.invoke({
    "movie_description": para
})
response = model.invoke(final_prompt)

# 6. Print the result
print(response.content)