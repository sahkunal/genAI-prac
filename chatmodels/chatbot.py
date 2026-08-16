from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

model = init_chat_model(
    "llama-3.1-8b-instant",
    model_provider="groq",
    temperature=0.7,
    max_tokens=100,
)
print("choose your AI mode")
print("1. angry")
print("2. funny")
print("3. sad")
choice = input("Enter your choice (1, 2, or 3): ")
if choice == "1":
    messages = [
        SystemMessage(content="You are an angry assistant.")
    ]
elif choice == "2": 
    messages = [
        SystemMessage(content="You are a funny assistant.")
    ]
elif choice == "3":
    messages = [
        SystemMessage(content="You are a sad assistant.")
    ]
else:
    print("Invalid choice. Defaulting to funny mode.")
messages = [
    SystemMessage(content=messages)
]

print("Type 'exit' to quit.")

while True:
    prompt = input("Enter your prompt: ")

    if prompt.lower() == "exit":
        break

    messages.append(HumanMessage(content=prompt))

    response = model.invoke(messages)

    messages.append(response)

    print("Bot:", response.content)