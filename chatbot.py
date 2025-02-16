import streamlit as st
import ollama

st.session_state.setdefault("Conversation_history", [])

def generate_response(user_input):
    st.session_state['Conversation_history'].append({'role': "user", "content": user_input})

    response = ollama.chat(model="llama3", messages=st.session_state['Conversation_history'])
    ai_response = response['message']['content']

    st.session_state['Conversation_history'].append({'role': 'assistant', "content": ai_response})
    return ai_response

st.title("Mental Health Chatbot")

for msg in st.session_state['Conversation_history']:
    role = "You" if msg['role'] == 'user' else "AI"
    st.markdown(f"**{role}:** {msg['content']}")

user_msg = st.text_input("How can I help you today?")

if user_msg:
    with st.spinner("Thinking..."):
        ai_response = generate_response(user_msg)
        st.markdown(f"**AI:** {ai_response}")
