from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate


# Model
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0
)


# Prompt template
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


# Chain
chain = prompt | model


# UI
st.title("Movie Description Extractor")

movie_description = st.text_area(
    "Enter the movie description:",
    height=300
)


if st.button("Extract Information"):

    if movie_description:
        response = chain.invoke({
            "movie_description": movie_description
        })

        st.subheader("Extracted Information")
        st.write(response.content)