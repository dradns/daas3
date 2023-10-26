import streamlit as st
from knowledge_gpt.components.sidebar import sidebar

from st_pages import Page, show_pages, Section, add_page_title
add_page_title()

from knowledge_gpt.ui import (
    wrap_doc_in_html,
    is_query_valid,
    is_file_valid,
    is_open_ai_key_valid,
    display_file_read_error,
)

from knowledge_gpt.core.caching import bootstrap_caching
from knowledge_gpt.core.parsing import read_file
from knowledge_gpt.core.chunking import chunk_file
from knowledge_gpt.core.embedding import embed_files
from knowledge_gpt.core.qa import query_folder
from knowledge_gpt.core.utils import get_llm

EMBEDDING = "openai"
VECTOR_STORE = "faiss"
MODEL_LIST = ["gpt-3.5-turbo", "gpt-4"]

# Uncomment to enable debug mode
# MODEL_LIST.insert(0, "debug")

#TITLES
st.set_page_config(page_title="DAAS", page_icon="📖", layout="wide")
st.header("📖User Story")
#SUBHEADER
st.warning(
        "Lets write business requirements")

#DECLARE BUTTON RESET HISTORY
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

#USAGE BUTTON RESET HISTORY
st.button('Forgot context', on_click=clear_chat_history)

# Enable caching for expensive functions
bootstrap_caching()

sidebar()

openai_api_key = st.session_state.get("OPENAI_API_KEY")

model: str = st.selectbox("Model", options=MODEL_LIST)  # type: ignore

with st.expander("Advanced Options"):
    return_all_chunks = st.checkbox("Show all chunks retrieved from vector search")
    show_full_doc = st.checkbox("Show parsed contents of the document")

st.markdown("---")

st.header("📖Use Case")