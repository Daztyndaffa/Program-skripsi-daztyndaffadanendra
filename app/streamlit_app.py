import sys
import os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.rag.generator import generate_answer


# ================================
# PAGE CONFIG
# ================================

st.set_page_config(
    page_title="AI Assistant UIR",
    page_icon="🎓",
    layout="centered"
)


# ================================
# CUSTOM CSS
# ================================

st.markdown("""
<style>

body {
    background-color: #F5F7F6;
}

.main {
    background-color: #F5F7F6;
}

/* USER CHAT */
.user-bubble {
    background-color: #0B5E3C;
    color: white;
    padding: 12px 16px;
    border-radius: 16px;
    margin: 8px 0;
    width: fit-content;
    max-width: 70%;
    margin-left: auto;
}

/* AI CHAT */
.ai-bubble {
    background-color: #E8F3EE;
    color: #083F2A;
    padding: 12px 16px;
    border-radius: 16px;
    margin: 8px 0;
    width: fit-content;
    max-width: 70%;
}

.title {
    color: #0B5E3C;
    text-align: center;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #555;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# ================================
# TITLE
# ================================

st.markdown("<h1 class='title'>AI Assistant Universitas Islam Riau</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Hai!! Saya AI Assistant UIR. Silahkan tanyakan informasi seputar UIR ya!!!</p>", unsafe_allow_html=True)


# ================================
# CHAT HISTORY
# ================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ================================
# DISPLAY CHAT
# ================================

for msg in st.session_state.messages:

    if msg["role"] == "user":

        st.markdown(
            f"<div class='user-bubble'> {msg['content']}</div>",
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"<div class='ai-bubble'> {msg['content']}</div>",
            unsafe_allow_html=True
        )


# ================================
# INPUT
# ================================

question = st.chat_input("Tanyakan sesuatu...")

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.spinner("AI sedang mencari jawaban..."):
        answer = generate_answer(question)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()