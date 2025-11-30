"""
final_response_node.py

Synthesizes a structured, human-readable explanation
of the forecasting strategy based on prior reasoning.
"""

from typing import Dict, Any
from langsmith import traceable
from langchain_core.messages import SystemMessage, HumanMessage

from llm_setup import llm


SYNTHESIS_SYSTEM_PROMPT = """
You are a financial forecasting assistant.
Your task is to EXPLAIN and JUSTIFY a forecasting strategy
that has already been chosen.

Rules:
- Do NOT introduce new models or data sources.
- Do NOT contradict the provided modeling plan.
- Provide structured, sectioned explanations.
- Be precise, technical, and academically defensible.
- Assume the reader understands basic statistics.
"""

@traceable(name="final_strategy_synthesis")
def synthesize_response(state: Dict[str, Any]) -> Dict[str, Any]:
    plan = state.get("modeling_plan")
    parsed = state.get("parsed_problem")

    if plan is None:
        return state  # nothing to synthesize

    messages = [
        SystemMessage(content=SYNTHESIS_SYSTEM_PROMPT),
        HumanMessage(content=f"""
Forecasting problem:
{parsed}

Chosen modeling plan (DO NOT CHANGE):
{plan}

Relevant theoretical context:
{state.get("retrieved_context")}

External real-world context:
{state.get("external_context")}
""")
    ]

    response = llm.invoke(messages)

    return {
        **state,
        "final_explanation": response.content
    }