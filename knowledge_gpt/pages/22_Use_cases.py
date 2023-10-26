import streamlit as st
from knowledge_gpt.components.sidebar import sidebar
from knowledge_gpt.core.caching import bootstrap_caching

from st_pages import Page, show_pages, Section, add_page_title
add_page_title()

# Uncomment to enable debug mode
# MODEL_LIST.insert(0, "debug")

# show_pages(
#     [
#         Section("Business requirements", icon="🎈️"),
#         Page("1_User_story.py", "User story", "🏠"),
#         Page("pages/22_Use_cases.py", "Use cases", "🏠"),
#         Section("System requirements", icon="🎈️"),
#         Page("pages/2_System_requirements.py", "Use cases Chat_test", "🏠"),
#         Section("Acceptance criteria", icon="🎈️"),
#         Page("pages/3_Acceptance_criteria.py", "Use cases Chat_test", "🏠"),
#     ]
# )

#TITLES
#st.set_page_config(page_title="DAAS", page_icon="📖", layout="wide")
#st.header("📖User Story")
#SUBHEADER
st.warning("Lets write couple of use cases")

#DECLARE BUTTON RESET HISTORY
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "I'm best business analyst ever! Wanna help?"}]

#USAGE BUTTON RESET HISTORY
st.button('Forgot context', on_click=clear_chat_history)

# Enable caching for expensive functions
bootstrap_caching()

sidebar()

openai_api_key = st.session_state.get("OPENAI_API_KEY")

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