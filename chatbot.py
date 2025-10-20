

from openai import OpenAI
from openai import OpenAIError  # v2.6.0 uses this for all API errors

# 🔑 Replace this with your actual OpenAI API key
client = OpenAI(api_key="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")

print("Welcome to the LLM Chatbot! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        print("Bot:", response.choices[0].message.content)

    except OpenAIError as e:
        print(f"Bot: ⚠ An error occurred: {e}")
        break
