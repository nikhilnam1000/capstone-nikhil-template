import streamlit as st
from pprint import pprint

from graph import graph


st.set_page_config(
    page_title="Financial Forecasting Assistant",
    layout="wide"
)

st.title("📈 Financial Forecasting Assistant")
st.markdown(
    "Provide a forecasting problem statement. "
    "The assistant will either ask for clarification or propose a modeling strategy."
)

# User input
user_query = st.text_area(
    "Forecasting Problem",
    placeholder="e.g. Forecast monthly inflation for India for the next 12 months using macroeconomic data."
)

run_button = st.button("Run Assistant")

if run_button and user_query.strip():

    with st.spinner("Analyzing problem..."):
        final_state = graph.invoke(
            {"user_query": user_query}
        )

    st.divider()

    # 1. Clarification questions
    clarifications = final_state.get("clarification_questions", [])
    if clarifications:
        st.subheader("🔍 Clarification Required")
        for q in clarifications:
            st.warning(q)
        st.stop()

    # 2. Final synthesized explanation (PRIMARY OUTPUT)
    final_text = final_state.get("final_explanation")
    if final_text:
        st.subheader("📘 Forecasting Strategy Explanation")
        st.markdown(final_text)

    # 3. Modeling plan
    plan = final_state.get("modeling_plan")
    if plan:
        with st.expander("🔎 View Structured Modeling Plan"):
            st.markdown("### Recommended Models")
            st.write(plan.recommended_models)

            st.markdown("### Data Requirements")
            st.write(plan.data_requirements)

            st.markdown("### Preprocessing Steps")
            st.write(plan.preprocessing_steps)

            st.markdown("### Feature Engineering")
            st.write(plan.feature_engineering)

            st.markdown("### Regularization Strategy")
            st.write(plan.regularization_strategy)

            st.markdown("### Evaluation Metrics")
            st.write(plan.evaluation_metrics)

            st.markdown("### Interpretation Guidelines")
            st.write(plan.interpretation_guidelines)

    # 3. External context (Tavily)
    external = final_state.get("external_context")
    if external:
        st.subheader("🌐 Relevant External Sources")

        for item in external:
            st.markdown(f"**{item.get('title', 'Source')}**")
            st.markdown(item.get("url", ""))
            st.caption(item.get("content", "")[:500] + "…")

    # Optional debug
    with st.expander("🔧 Debug: Full State"):
        pprint(final_state)