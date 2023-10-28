import os
import streamlit as st
from knowledge_gpt.components.sidebar import sidebar
from knowledge_gpt.core.caching import bootstrap_caching
from st_pages import Page, show_pages, Section, add_page_title
from knowledge_gpt.functions.llama2 import model_response
from huggingface_hub import InferenceClient

add_page_title()

show_pages(
    [
        Section("Business requirements", icon="👔 "),
        Page("1_User_story.py", "User story", "🗣️"),
        Page("pages/22_Use_cases.py", "Use case", "✒️"),
        Section("System requirements", icon="⚙️️"),
        Page("pages/2_System_requirements.py", "Use cases Chat_test", "🏠"),
        Section("Acceptance criteria", icon="✔️️"),
        Page("pages/3_Acceptance_criteria.py", "Use cases Chat_test", "🏠"),
        Page("pages/5_Mermaid_test.py", "Mermaid", "🏠"),
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
#USAGE BUTTON RESET HISTORY
st.button('Forgot context', on_click=clear_chat_history)

# Enable caching for expensive functions
bootstrap_caching()
# Render sidebar
sidebar()

api_key = st.session_state.get("API_KEY")
#st.session_state["API_KEY"] = 'r8_5dXks0XSi27sUU4zxiCeKiYOB1wvfil3UZOxV'
replicate_api = st.session_state.get("API_KEY")
os.environ['REPLICATE_API_TOKEN'] = replicate_api
print('API KEY')
print(st.session_state.get("API_KEY"))

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "I'm best business analyst ever! Wanna help?"}]

# Display or clear chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model_response(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)

print(st.session_state.get("API_KEY"))