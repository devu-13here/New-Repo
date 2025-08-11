# ────────────────────────────────────────────────────────────────────────────────
#  Claude Chatbot • Streamlit front‑end
#  Requirements  : streamlit >= 1.25  •  anthropic
# ────────────────────────────────────────────────────────────────────────────────
import os
import streamlit as st
import anthropic

# ─── 1) Get API key and initialize client ─────────────────────────────────────
# The anthropic client defaults to os.environ.get("ANTHROPIC_API_KEY")
# We add a check to provide a user-friendly error message if the key is not set.
if not os.environ.get("ANTHROPIC_API_KEY"):
    st.error("`ANTHROPIC_API_KEY` environment variable not set.")
    st.stop()

try:
    client = anthropic.Anthropic()
except Exception as e:
    st.error(f"Failed to initialize Anthropic client: {e}")
    st.stop()

# ─── 2) Streamlit page & sidebar ───────────────────────────────────────────────
st.set_page_config(page_title="Claude Chatbot", page_icon="🤖", layout="centered")

with st.sidebar:
    st.title("🤖 Claude Chatbot")
    st.caption("Powered by Anthropic")
    st.markdown("---")
    temperature = st.slider("Creativity (temperature)", 0.0, 1.0, 0.7, 0.1)
    max_tokens = st.slider("Max tokens in reply", 1, 4096, 512, 10)
    if st.button("🗑 Clear chat"):
        st.session_state.pop("history", None)
        st.rerun()

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

    # ---- call API ----
    try:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = client.messages.create(
                    model="claude-3-haiku-20240307",
                    messages=st.session_state.history,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                assistant_reply = response.content[0].text
                st.write(assistant_reply)

        # ---- remember assistant reply ----
        st.session_state.history.append({"role": "assistant", "content": assistant_reply})

    except anthropic.APIError as e:
        st.error(f"Anthropic API error: {e.status_code} {e.response.text}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
