import os

import streamlit as st
from knowledge_gpt.components.sidebar import sidebar
from knowledge_gpt.core.caching import bootstrap_caching

from st_pages import Page, show_pages, Section, add_page_title
add_page_title()

# Enable caching for expensive functions
bootstrap_caching()

sidebar()

api_key = st.session_state.get("API_KEY")

if not api_key:
    st.warning(
        "Enter your API key in the sidebar. You can get a key at")

api_key_input = st.text_input(
            "API Key",
            type="password",
            placeholder="Paste your API key here ",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
            value=os.environ.get("API_KEY", None)
            or st.session_state.get("API_KEY", ""),
        )

st.session_state["API_KEY"] = api_key_input

st.subheader('Models and parameters')
selected_model = st.selectbox('Choose a Llama2 model', ['Llama2-7B', 'Llama2-13B'], key='selected_model')
if selected_model == 'Llama2-7B':
    llm = 'a16z-infra/llama7b-v2-chat:4f0a4744c7295c024a1de15e1a63c880d3da035fa1f49bfd344fe076074c8eea'
elif selected_model == 'Llama2-13B':
    llm = 'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5'
temperature = st.slider('temperature', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
top_p = st.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
max_length = st.slider('max_length', min_value=32, max_value=128, value=120, step=8)
