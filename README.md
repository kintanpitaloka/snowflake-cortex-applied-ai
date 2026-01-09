# Applied AI Insight Assistant with Snowflake Cortex
## Streamlit Apps — 30 Days of Applied AI

This repository documents the progressive development of an end-to-end
Applied AI application using **Snowflake Cortex** and **Streamlit**.

The focus is not only on model inference, but on **production patterns**:
latency handling, UX feedback, caching, and interface design for real users.

---

## Day 1 — Snowflake Connection
Validated secure Streamlit-in-Snowflake execution:
- Active session detection
- Warehouse-backed compute
- End-to-end connectivity verification

---

## Day 2 — LLM Inference with Cortex (SQL)
Executed **Claude 3.5 Sonnet** using Snowflake Cortex via Snowpark:
- SQL-based LLM invocation
- Secure in-warehouse inference
- JSON response handling

---

## Day 3 — Streaming LLM Responses
Built a real-time LLM streaming interface.

**Key highlights:**
- Multi-model support (Claude, Mistral, LLaMA)
- Token-level streaming for improved UX
- Fallback generator for production compatibility

---

## Day 4 — Cached LLM Application
Implemented performance optimization patterns:
- Streamlit caching for repeated prompts
- Latency measurement and visibility
- Efficient Snowflake Cortex execution

---

## Day 5 — LinkedIn Post Generator
Developed an AI-powered content generation tool:
- Dynamic prompt engineering (tone, length, URL-based context)
- Cached inference for responsiveness
- Structured output for professional use cases

---

## Day 6 — Status UI for Long-Running AI Tasks
Enhanced user experience for slow AI operations:
- Real-time status indicators
- Clear task progression feedback
- UX patterns aligned with production AI systems

This mirrors real-world AI products where inference latency must be
explicitly communicated to users.

---

## Day 7 — Theming & Layout (Product Polish)
Transformed the functional AI tool into a **user-facing product**:
- Dark mode theming
- Sidebar-driven layout
- Clear separation of input, processing, and output
- Consistent visual hierarchy

**Focus:** product readiness, usability, and design clarity.

---

## Core Skills Demonstrated
- Applied LLM integration (Snowflake Cortex)
- Streaming & latency-aware AI UX
- Caching & performance optimization
- Human-centered interface design
- Secure, production-style deployment patterns
