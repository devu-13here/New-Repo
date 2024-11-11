import os
import json
import streamlit as st
import requests

# Load the Anthropic API key from the config file
working_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(working_dir, "config.json")

with open(config_file_path, "r") as config_file:
    config_data = json.load(config_file)

# Retrieve the API key from the config file
ANTHROPIC_API_KEY = config_data["ANTHROPIC_API_KEY"]

# Streamlit page configuration
st.set_page_config(
    page_title="Claude Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Streamlit sidebar for additional options
with st.sidebar:
    st.title("🤖 Claude Chatbot")
    st.write("Powered by Anthropic's Claude model")
    st.write("Use this chatbot to interact with the Claude AI model. Feel free to ask any questions!")
    st.markdown("---")
    st.write("### Chat Settings")
    temperature = st.slider("Response Creativity (Temperature)", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
    max_tokens = st.slider("Max Tokens (Response Length)", min_value=50, max_value=500, value=200, step=50)

# Initialize chat history if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Page title
st.markdown("<h1 style='text-align: center;'>🤖 Claude AI Chatbot</h1>", unsafe_allow_html=True)

# Show chat history
for message in st.session_state.chat_history:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(f"<div style='background-color: #e0f7fa; padding: 10px; border-radius: 10px;'>{message['content']}</div>", unsafe_allow_html=True)
    else:
        with st.chat_message("assistant"):
            st.markdown(f"<div style='background-color: #f1f8e9; padding: 10px; border-radius: 10px;'>{message['content']}</div>", unsafe_allow_html=True)

# Input field for user's message
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user's message to chat history and display it
    st.chat_message("user").markdown(f"<div style='background-color: #e0f7fa; padding: 10px; border-radius: 10px;'>{user_input}</div>", unsafe_allow_html=True)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Send user's message to Claude API
    try:
        headers = {
            "x-api-key": ANTHROPIC_API_KEY,
            "Content-Type": "application/json"
        }

        # Prepare the conversation history for Claude
        chat_history_text = "\n\n".join([f"Human: {msg['content']}\nAssistant:" if msg["role"] == "assistant" else f"Human: {msg['content']}" for msg in st.session_state.chat_history])

        # API Payload
        payload = {
            "prompt": f"{chat_history_text}\nHuman: {user_input}\nAssistant:",
            "model": "claude-v1.3",  # Make sure the model name is correct
            "temperature": temperature,
            "max_tokens_to_sample": max_tokens,
            "stop_sequences": ["\nHuman:"]
        }

        # API Request to Anthropic
        response = requests.post("https://api.anthropic.com/v1/complete", headers=headers, json=payload)

        # Check for a successful response
        if response.status_code == 200:
            response_json = response.json()
            assistant_reply = response_json.get("completion", "Sorry, I couldn't process that.")
        else:
            assistant_reply = f"Error: {response.status_code} - {response.text}"

        # Add the assistant's response to chat history and display it
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_reply})
        with st.chat_message("assistant"):
            st.markdown(f"<div style='background-color: #f1f8e9; padding: 10px; border-radius: 10px;'>{assistant_reply}</div>", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Clear the chat session button
if st.sidebar.button("Clear Chat"):
    st.session_state.chat_history = []
    st.experimental_rerun()
