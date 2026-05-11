import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

API_KEY = os.getenv("API_KEY")


genai.configure(api_key=API_KEY)


model = genai.GenerativeModel("gemini-2.5-flash")


chat = model.start_chat(history=[])

print("Gemini Chatbot")
print("Type 'exit' to stop.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = chat.send_message(user_input)

    print("Bot:", response.text)