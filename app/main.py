import streamlit as st
from pathlib import Path
from faq import ingest_faq_data, faq_chain
from sql import sql_chain
from router import router

st.markdown(
    """
    <div style='text-align: center; font-size: 12px; color: gray;'>
        Created By Rohesen ♥️
    </div>
    """,
    unsafe_allow_html=True
)

# Load FAQ data
faqs_path = Path(__file__).parent / "resources/faq_data.csv"
ingest_faq_data(faqs_path)

# Query routing logic
def ask(query):
    route = router(query).name
    if route == 'faq':
        return faq_chain(query)
    elif route == 'sql':
        return sql_chain(query)
    else:
        return f"❌ Route '{route}' not implemented yet."

# Streamlit app UI
st.title("🛍️ E-commerce ChatBot")

# Capture user input
query = st.chat_input("💬 Write your query here...")

# Initialize session messages
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Process new query
if query:
    # Display user message
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})

    # Get and display response
    response = ask(query)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})



