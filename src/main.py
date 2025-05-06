# ────────────────────────────────────────────────────────────────────────────────
#  Claude Chatbot • Streamlit front‑end
#  Requirements  : streamlit >= 1.25  •  requests
# ────────────────────────────────────────────────────────────────────────────────
import json
import os
from pathlib import Path

import requests
import streamlit as st

# ─── 1) Load API key ────────────────────────────────────────────────────────────
def load_api_key() -> str:
    """Return Anthropic API key (env var wins, else config.json)."""
    if "ANTHROPIC_API_KEY" in os.environ:
        return os.environ["ANTHROPIC_API_KEY"]

    cfg_path = Path(__file__).with_name("config.json")
    try:
        with cfg_path.open() as f:
            return json.load(f)["ANTHROPIC_API_KEY"]
    except FileNotFoundError:
        st.error("`config.json` not found and env var `ANTHROPIC_API_KEY` missing.")
        st.stop()
    except KeyError:
        st.error("`ANTHROPIC_API_KEY` key missing in config.json.")
        st.stop()


API_KEY = load_api_key()

# ─── 2) Streamlit page & sidebar ───────────────────────────────────────────────
st.set_page_config(page_title="Claude Chatbot", page_icon="🤖", layout="centered")

with st.sidebar:
    st.title("🤖 Claude Chatbot")
    st.caption("Powered by Anthropic")
    st.markdown("---")
    temperature = st.slider("Creativity (temperature)", 0.0, 1.0, 0.7, 0.1)
    max_tokens = st.slider("Max tokens in reply", 1, 500, 200, 10)
    if st.button("🗑 Clear chat"):
        st.session_state.pop("history", None)
        st.experimental_rerun()

# ─── 3) Session state for history ──────────────────────────────────────────────
if "history" not in st.session_state:
    # each item: {"role": "user"|"assistant", "content": "..."}
    st.session_state.history = []

# ─── 4) Show chat so far ───────────────────────────────────────────────────────
st.markdown("<h1 style='text-align:center;'>🤖 Claude Chatbot</h1>",
            unsafe_allow_html=True)

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ─── 5) User input box ─────────────────────────────────────────────────────────
user_text = st.chat_input("Type your message…")

# ─── 6) If user sent a message, call Anthropic API ─────────────────────────────
if user_text:
    # add user line to history & echo to UI
    st.session_state.history.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.write(user_text)

    # ---- build prompt in Anthropic “alternating” format ----
    prompt_lines = []
    for item in st.session_state.history:
        who = "Human" if item["role"] == "user" else "Assistant"
        prompt_lines.append(f"{who}: {item['content']}")
    prompt_lines.append("Assistant:")          # Claude should answer next
    prompt = "\n\n".join(prompt_lines)

    # ---- call API ----
    payload = {
        "model": "claude-v1.3",
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens_to_sample": max_tokens,
        "stop_sequences": ["\nHuman:"]
    }
    headers = {
        "x-api-key": API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    try:
        r = requests.post("https://api.anthropic.com/v1/complete",
                          headers=headers, json=payload, timeout=30)
        r.raise_for_status()
        assistant_reply = r.json()["completion"].strip()
    except requests.exceptions.RequestException as e:
        assistant_reply = f"API error: {e}"

    # ---- display & remember assistant reply ----
    st.session_state.history.append({"role": "assistant",
                                     "content": assistant_reply})
    with st.chat_message("assistant"):
        st.write(assistant_reply)
