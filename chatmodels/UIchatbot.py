import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="AI Mood Chatbot",
    page_icon="💬",
    layout="centered",
)


# -----------------------------
# Custom CSS
# -----------------------------
st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background: #0e1117;
    }

    /* Main content width */
    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 5rem;
    }

    /* Header */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #9ca3af;
        font-size: 16px;
        margin-bottom: 30px;
    }

    /* Mode card */
    .mode-card {
        padding: 18px;
        border-radius: 15px;
        background: #161b22;
        border: 1px solid #30363d;
        margin-bottom: 25px;
    }

    .mode-title {
        font-size: 14px;
        color: #9ca3af;
        margin-bottom: 5px;
    }

    .mode-name {
        font-size: 22px;
        font-weight: 600;
    }

    /* Chat input */
    .stChatInput {
        bottom: 20px;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# Model
# -----------------------------
@st.cache_resource
def get_model():
    return init_chat_model(
        "llama-3.1-8b-instant",
        model_provider="groq",
        temperature=0.7,
        max_tokens=100,
    )


model = get_model()


# -----------------------------
# Mood configuration
# -----------------------------
modes = {
    "😡 Angry": "You are an angry assistant.",
    "😂 Funny": "You are a funny assistant.",
    "😢 Sad": "You are a sad assistant.",
}


# -----------------------------
# Initialize session state
# -----------------------------
if "mode" not in st.session_state:
    st.session_state.mode = "😂 Funny"

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(
            content=modes[st.session_state.mode]
        )
    ]


# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="main-title">💬 AI Mood Chatbot</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">Choose a mood and start chatting</div>',
    unsafe_allow_html=True,
)


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("⚙️ Settings")

    selected_mode = st.radio(
        "Choose AI mode",
        list(modes.keys()),
        index=list(modes.keys()).index(st.session_state.mode),
    )

    st.divider()

    if st.button("🗑️ New Chat", use_container_width=True):

        st.session_state.mode = selected_mode

        st.session_state.messages = [
            SystemMessage(
                content=modes[selected_mode]
            )
        ]

        st.rerun()


# -----------------------------
# Handle mode change
# -----------------------------
if selected_mode != st.session_state.mode:

    st.session_state.mode = selected_mode

    st.session_state.messages = [
        SystemMessage(
            content=modes[selected_mode]
        )
    ]

    st.rerun()


# -----------------------------
# Current mode display
# -----------------------------
st.markdown(
    f"""
    <div class="mode-card">
        <div class="mode-title">CURRENT AI MODE</div>
        <div class="mode-name">{st.session_state.mode}</div>
    </div>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# Display chat history
# -----------------------------
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):
            st.write(message.content)


# -----------------------------
# Chat input
# -----------------------------
prompt = st.chat_input("Type your message...")


if prompt:

    # Add user message
    human_message = HumanMessage(content=prompt)

    st.session_state.messages.append(human_message)

    with st.chat_message("user"):
        st.write(prompt)

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = model.invoke(
                st.session_state.messages
            )

            st.write(response.content)

    # Save response
    st.session_state.messages.append(response)