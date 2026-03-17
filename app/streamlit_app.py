import streamlit as st
import requests

API_URL = "http://backend:8000/ask"

st.title("Training Knowledge Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask a question")

if user_input:
    st.session_state.messages.append(("user", user_input))

    try:
        response = requests.post(
            API_URL,
            json={"question": user_input},
            timeout=60  
        )

        if response.status_code == 200:
            data = response.json()

            answer = data.get("answer", "No answer returned.")
            source = data.get("source", "")

            if source == "local_llm":
                answer += "\n\n⚠️ Running in local fallback mode"

        else:
            answer = f"Server error {response.status_code}"

    except Exception as e:
        answer = f"Request failed: {e}"

    st.session_state.messages.append(("assistant", answer))


# Display messages
for role, msg in st.session_state.messages:
    st.chat_message(role).write(msg)