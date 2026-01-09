# Applied AI Insight Assistant with Snowflake Cortex

This project demonstrates how to build an applied AI application using
**Snowflake Cortex** and **Streamlit** to support decision-making and insight generation.

The app connects directly to Snowflake, validates the session, and runs
large language model (LLM) inference **inside the data platform** — without external APIs.

---

## 🔍 What This Project Shows

- Secure connection to Snowflake using Snowpark
- Running LLM inference directly in Snowflake via Cortex
- Streamlit-based interface for human-centered AI interaction
- Environment-agnostic setup (Snowflake, local, or Streamlit Community Cloud)

---

## 🧠 Use Case Orientation

This project is designed as a foundation for:
- AI-powered insight assistants
- Decision-support tools for analysts
- Behavioral & business intelligence copilots
- Applied AI prototypes inside data platforms

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **Snowflake Snowpark**
- **Snowflake Cortex (Claude 3.5 Sonnet)**

---

## 🚀 App Features

### 1. Snowflake Connection Validation
Confirms active Snowflake session and displays platform version.

### 2. AI Insight Generation
Accepts user prompts and generates responses using Snowflake Cortex LLMs,
executed directly within Snowflake.
