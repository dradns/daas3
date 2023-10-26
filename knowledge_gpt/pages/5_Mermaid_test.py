import os
import streamlit as st
from knowledge_gpt.components.sidebar import sidebar
from knowledge_gpt.core.caching import bootstrap_caching
import streamlit_mermaid as stmd

from st_pages import Page, show_pages, Section, add_page_title
add_page_title()


EMBEDDING = "openai"
VECTOR_STORE = "faiss"
MODEL_LIST = ["gpt-3.5-turbo", "gpt-4"]

# Uncomment to enable debug mode
# MODEL_LIST.insert(0, "debug")

st.set_page_config(page_title="DAAS", page_icon="📖", layout="wide")
st.header("LLM key")

# Enable caching for expensive functions
bootstrap_caching()

sidebar()

openai_api_key = st.session_state.get("OPENAI_API_KEY")

if not openai_api_key:
    st.warning(
        "Enter your OpenAI API key in the sidebar. You can get a key at"
        " https://platform.openai.com/account/api-keys."
    )

api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            key="efer",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
            value=os.environ.get("OPENAI_API_KEY", None)
            or st.session_state.get("OPENAI_API_KEY", ""),
        )

st.session_state["OPENAI_API_KEY"] = api_key_input

code = """
sequenceDiagram
    participant Client
    participant Server
    participant Database

    Client->>Server: Request (Post Status Update)
    Server->>Database: Insert Status Update
    Database-->>Server: Acknowledge Insert
    Server-->>Client: Response (Status Update Successful)
"""

mermaid = stmd.st_mermaid(code)
st.write(mermaid)
