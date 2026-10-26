import os
import time
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    timeout=20.0,
    max_retries=0,
)

print("Sending request to Groq...")
start = time.perf_counter()

try:
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": "Hi! Reply in one short sentence."}
        ],
        max_tokens=50,
    )

    elapsed = time.perf_counter() - start

    print("\nResponse:", response.choices[0].message.content)
    print(f"API request time: {elapsed:.2f} seconds")

    if response.usage:
        print("Input tokens:", response.usage.prompt_tokens)
        print("Output tokens:", response.usage.completion_tokens)

except Exception as e:
    elapsed = time.perf_counter() - start
    print(f"\nFailed after {elapsed:.2f} seconds")
    print("Error type:", type(e).__name__)
    print("Error:", e)