import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    st.error("No API Key found!")
    st.stop()


genai.configure(api_key=API_KEY)


model = genai.GenerativeModel("gemini-2.5-flash")


if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "history" not in st.session_state:
    st.session_state.history = []

chat = st.session_state.chat


st.title("Gemini Chatbot")


user_message = st.text_input("Ask me anything:")


if st.button("Send") and user_message:

    response = chat.send_message(user_message)

    st.session_state.history.append(
        {"user": user_message, "bot": response.text}
    )

for msg in st.session_state.history:
    st.write("You:", msg["user"])
    st.write("Bot:", msg["bot"])