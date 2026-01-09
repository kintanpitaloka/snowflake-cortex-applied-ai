import streamlit as st
import json
from snowflake.snowpark.functions import ai_complete

# -----------------------------------
# Connect to Snowflake
# -----------------------------------
try:
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    from snowflake.snowpark import Session
    session = Session.builder.configs(
        st.secrets["connections"]["snowflake"]
    ).create()

# -----------------------------------
# Cached Cortex Call
# -----------------------------------
@st.cache_data(show_spinner=False)
def call_cortex_llm(prompt_text: str) -> str:
    model = "claude-3-5-sonnet"

    df = session.range(1).select(
        ai_complete(model=model, prompt=prompt_text).alias("response")
    )

    raw = df.collect()[0][0]
    parsed = json.loads(raw)

    # Extract clean text
    return parsed["choices"][0]["messages"]

# -----------------------------------
# UI
# -----------------------------------
st.title("📝 LinkedIn Post Generator v2")
st.caption("Snowflake Cortex · Status-aware AI UX")

content = st.text_input(
    "Content URL",
    "https://docs.snowflake.com/en/user-guide/views-semantic/overview"
)

tone = st.selectbox(
    "Tone",
    ["Professional", "Casual", "Funny"]
)

word_count = st.slider(
    "Approximate word count",
    50, 300, 100
)

# -----------------------------------
# Generate Flow
# -----------------------------------
if st.button("Generate Post"):

    with st.status("🚀 Generating LinkedIn post...", expanded=True) as status:

        status.write("🧠 Analyzing tone & constraints...")
        prompt = f"""
You are an expert social media manager.

Create a LinkedIn post using:
- Source URL: {content}
- Tone: {tone}
- Length: ~{word_count} words

Rules:
- Clear and engaging
- Short paragraphs
- Use dash (-) for bullets
- Output ONLY the LinkedIn post text
"""

        status.write("🤖 Calling Snowflake Cortex (Claude 3.5 Sonnet)...")
        post = call_cortex_llm(prompt)

        status.update(
            label="✅ Post generated successfully!",
            state="complete",
            expanded=False
        )

    st.subheader("Generated LinkedIn Post")
    st.markdown(post)
