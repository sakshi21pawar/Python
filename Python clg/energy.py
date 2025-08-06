import os
import streamlit as st
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Gemini API Key setup
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"] if "GOOGLE_API_KEY" in st.secrets else os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash-latest", temperature=0.2)

# LangGraph nodes
def get_user_query(state: dict) -> dict:
    state["query"] = st.session_state.user_input
    return state

def energy_advice(state: dict) -> dict:
    prompt = (
        "You are an expert Energy Advisor chatbot. Help users with:\n"
        "- Saving electricity\n"
        "- Recommending energy-efficient appliances\n"
        "- Explaining renewable energy options\n\n"
        f"User: {state['query']}"
    )
    response = llm.invoke([HumanMessage(content=prompt)])
    state["response"] = response.content.strip()
    return state

# Build graph
builder = StateGraph(dict)
builder.set_entry_point("get_user_query")
builder.add_node("get_user_query", get_user_query)
builder.add_node("energy_advice", energy_advice)
builder.add_edge("get_user_query", "energy_advice")
builder.add_edge("energy_advice", END)

graph = builder.compile()

# Streamlit UI
st.title("⚡ Energy Advisor Chatbot")
st.markdown("Ask questions like:\n- How to reduce electricity bill?\n- What is solar energy?\n- Best appliances to save power?")

user_input = st.text_input("Enter your question about energy saving:")
st.session_state.user_input = user_input

if st.button("Ask"):
    if user_input:
        final_state = graph.invoke({})
        st.markdown("### ✅ Answer:")
        st.write(final_state["response"])
