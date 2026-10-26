
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    max_tokens=100,
)

print("Choose your AI mode")
print("1. Angry")
print("2. Funny")
print("3. Sad")

choice = input("Enter your choice (1, 2, or 3): ")

if choice == "1":
    system_prompt = "You are an angry assistant."
elif choice == "2":
    system_prompt = "You are a funny assistant."
elif choice == "3":
    system_prompt = "You are a sad assistant."
else:
    print("Invalid choice. Defaulting to funny mode.")
    system_prompt = "You are a funny assistant."

messages = [
    SystemMessage(content=system_prompt)
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
