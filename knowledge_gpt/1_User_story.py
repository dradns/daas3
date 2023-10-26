import os

import streamlit as st
import replicate
from knowledge_gpt.components.sidebar import sidebar
from knowledge_gpt.core.caching import bootstrap_caching

from st_pages import Page, show_pages, Section, add_page_title
add_page_title()

# Uncomment to enable debug mode
# MODEL_LIST.insert(0, "debug")

show_pages(
    [
        Section("Business requirements", icon="👔 "),
        Page("1_User_story.py", "User story", "🗣️"),
        Page("pages/22_Use_cases.py", "Use case", "✒️"),
        Section("System requirements", icon="⚙️️"),
        Page("pages/2_System_requirements.py", "Use cases Chat_test", "🏠"),
        Section("Acceptance criteria", icon="✔️️"),
        Page("pages/3_Acceptance_criteria.py", "Use cases Chat_test", "🏠"),
        Section("Settings", icon="✔️️"),
        Page("pages/4_Settings.py", "Settings", "🏠"),

    ]
)

#TITLES
#st.set_page_config(page_title="DAAS", page_icon="📖", layout="wide")
#st.header("📖User Story")
#SUBHEADER
st.warning("Lets write couple of user stories")

#DECLARE BUTTON RESET HISTORY
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "I'm best business analyst ever! Wanna help?"}]

# Function for generating LLaMA2 response. Refactored from https://github.com/a16z-infra/llama2-chatbot

temperature = 0.01
top_p = 0.1
max_length = 120


def generate_llama2_response(prompt_input):
    string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',
                           input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
                                  "temperature":temperature, "top_p":top_p, "max_length":max_length, "repetition_penalty":1})
    return output

#USAGE BUTTON RESET HISTORY
st.button('Forgot context', on_click=clear_chat_history)

#st.button('Forgot context', on_click=clear_chat_history)
#print(st.session_state.get("API_KEY")) проверка апи кея



# Enable caching for expensive functions
bootstrap_caching()

sidebar()

api_key = st.session_state.get("API_KEY")
st.session_state["API_KEY"] = 'r8_5dXks0XSi27sUU4zxiCeKiYOB1wvfil3UZOxV'
replicate_api = st.session_state.get("API_KEY")
os.environ['REPLICATE_API_TOKEN'] = replicate_api

print("replicate api")
print(replicate_api)
#CHAT
# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "I'm best business analyst ever! Wanna help?"}]

# Display or clear chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User-provided prompt
if prompt := st.chat_input():#disabled=not replicate_api:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_llama2_response(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)


#st.markdown("---")
#st.header("📖Use Case")