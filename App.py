import streamlit as st

st.set_page_config(page_title="J.A.R.V.I.S. Core", page_icon="🤖", layout="centered")

st.markdown("<h1 style='text-align: center; color: #00ffcc;'>J.A.R.V.I.S.</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>AI Virtual Assistant v1.0 - All Systems Online</p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello Sir, J.A.R.V.I.S. is online. How can I assist you?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your command for J.A.R.V.I.S..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if "hello" in prompt.lower() or "hi" in prompt.lower():
            response = "Greetings, Sir. All primary systems are functioning at 100%."
        elif "status" in prompt.lower():
            response = "Power: Stable | Core: Online | Security: Active, Sir."
        else:
            response = f"Command received and processed, Sir: '{prompt}'"
        
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
