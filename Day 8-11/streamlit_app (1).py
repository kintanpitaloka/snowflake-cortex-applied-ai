import streamlit as st
import json
from snowflake.snowpark.functions import ai_complete

# --- Snowflake Connection ---
try:
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()

# --- LLM Call ---
def call_llm(prompt_text: str) -> str:
    df = session.range(1).select(
        ai_complete(model="claude-3-5-sonnet", prompt=prompt_text).alias("response")
    )
    response_raw = df.collect()[0][0]
    try:
        response_json = json.loads(response_raw)
        if isinstance(response_json, dict):
            return response_json.get("choices", [{}])[0].get("messages", "")
        return str(response_json)
    except:
        return str(response_raw)

# --- Page Config ---
st.set_page_config(
    page_title="Kinzzie Chatbot 💬",
    page_icon="🤖",
    layout="wide"
)

st.title("Kinzzie Chatbot 💜")
st.markdown("Your friendly Gen Z AI buddy 🤖✨")

# --- Initialize Messages ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Heyyy! 🌟 I'm Kinzzie, your AI buddy. What are we chatting about today?"}
    ]

# --- Sidebar Stats ---
with st.sidebar:
    st.header("Chat Stats 📊")
    user_msgs = len([m for m in st.session_state.messages if m["role"] == "user"])
    assistant_msgs = len([m for m in st.session_state.messages if m["role"] == "assistant"])
    st.metric("Your Messages", user_msgs)
    st.metric("AI Responses", assistant_msgs)
    
    if st.button("Clear History 🧹"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Heyyy! 🌟 I'm Kinzzie, your AI buddy. What are we chatting about today?"}
        ]

# --- Display all chat history with avatars ---
for msg in st.session_state.messages:
    if msg["content"].strip():  # skip empty
        avatar_icon = "🤖" if msg["role"] == "assistant" else "🧑"
        with st.chat_message(msg["role"], avatar=avatar_icon):
            st.markdown(msg["content"])

# --- Chat Input ---
if prompt := st.chat_input("Type your message here… ✨"):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)
    
    # Generate assistant response
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Kinzzie is thinking... ⏳"):
            history = st.session_state.messages[-5:]  # last 5 messages
            conversation = "\n\n".join([
                f"{'User' if m['role']=='user' else 'Assistant'}: {m['content']}" for m in history
            ])
            system_prompt = "You are Kinzzie, a friendly Gen Z AI chatbot helping the user."
            full_prompt = f"{system_prompt}\n\n{conversation}\n\nAssistant:"
            
            response = call_llm(full_prompt)
            st.markdown(response)
    
    # Append assistant response to session_state
    st.session_state.messages.append({"role": "assistant", "content": response})
st.divider()
st.caption("💜 Kinzzie Chatbot | @2026")
