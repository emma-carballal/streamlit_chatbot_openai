'''This chatbot uses the OpenAI ChatGPT API to correct German grammar in the responses to user's prompts.'''
import streamlit as st
import openai
import time

openai.api_key = st.secrets["OPENAI_API_KEY"]

# App title
st.set_page_config(page_title="💬 Grammatik ChatGPT")

"st.session_state:", st.session_state

# Choose OpenAI model
if "openai_model" not in st.session_state.keys():
    st.session_state.openai_model = "gpt-3.5-turbo"

# Initialize chat messages
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Hallo! Wie geht es dir?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
        #     message_placeholder.markdown(full_response + "▌")
        # message_placeholder.markdown(full_response)
    # Simulate stream of response with milliseconds delay
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)        
    st.session_state.messages.append({"role": "assistant", "content": full_response})
