import streamlit as st
import json
from snowflake.snowpark.functions import ai_complete

# -------------------------------
# Connect to Snowflake
# -------------------------------
try:
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    from snowflake.snowpark import Session
    session = Session.builder.configs(
        st.secrets["connections"]["snowflake"]
    ).create()

# -------------------------------
# Cached LLM Call
# -------------------------------
@st.cache_data(show_spinner=False)
def call_cortex_llm(prompt_text: str) -> str:
    """
    Calls Snowflake Cortex LLM and returns generated text.
    """
    model = "claude-3-5-sonnet"

    df = session.range(1).select(
        ai_complete(
            model=model,
            prompt=prompt_text
        ).alias("response")
    )

    response_raw = df.collect()[0][0]
    response_json = json.loads(response_raw)

    # Extract actual text output
    return response_json["choices"][0]["messages"]

# -------------------------------
# App UI
# -------------------------------
st.title("📝 AI-Powered LinkedIn Post Generator")

st.write(
    "Generate professional LinkedIn posts using Snowflake Cortex AI. "
    "Control tone, length, and content source with ease."
)

content_url = st.text_input(
    "Content URL",
    "https://docs.snowflake.com/en/user-guide/views-semantic/overview"
)

tone = st.selectbox(
    "Tone",
    ["Professional", "Casual", "Insightful", "Funny"]
)

word_count = st.slider(
    "Approximate word count",
    min_value=50,
    max_value=300,
    value=120
)

# -------------------------------
# Generate Post
# -------------------------------
if st.button("Generate LinkedIn Post"):
    prompt = f"""
You are a professional social media strategist.

Create a LinkedIn post based on the following:
- Content source: {content_url}
- Tone: {tone}
- Length: Approximately {word_count} words

Guidelines:
- Write in clear, engaging language
- Use short paragraphs
- Use dashes (-) for bullet points if needed
- Output only the LinkedIn post text
"""

    with st.spinner("Generating LinkedIn magic ✨"):
        post_text = call_cortex_llm(prompt)

    st.subheader("Generated Post")
    st.markdown(post_text)

# -------------------------------
# Footer
# -------------------------------
st.divider()
st.caption("Day 5 · LinkedIn Post Generator · Snowflake Cortex AI")
