import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

# ✅ Initialize LLM
llm = Ollama(model="gemma:2b")

# ✅ Define Prompt Template
prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful AI assistant. Answer the user's question based on the provided context.

    Context:
    {context}

    Question: {question}

    Provide a well-structured and concise answer:
    """
)

# ✅ Streamlit UI
st.title("Langchain gemma:2b Chatbot")
user_query = st.text_input("Ask me anything:")

if user_query:
    # Generate Response
    response = llm.invoke(prompt.format(context="General Knowledge", question=user_query))
    
    # Display Response
    st.write("**AI Response:**")
    st.write(response)
