import os
import streamlit as st
from knowledge_gpt.components.sidebar import sidebar
from knowledge_gpt.core.caching import bootstrap_caching
import streamlit_mermaid as stmd

from st_pages import Page, show_pages, Section, add_page_title
#add_page_title()

# Enable caching for expensive functions
bootstrap_caching()

sidebar()

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
