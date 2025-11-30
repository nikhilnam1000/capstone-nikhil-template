"""
strategy_node.py

LangGraph node responsible for proposing a detailed
forecasting strategy or requesting clarification.
"""

from typing import Dict, Any

from langchain_core.messages import SystemMessage, HumanMessage
from langsmith import traceable

from llm_setup import (
    ModelingPlan,
    STRATEGY_SYSTEM_PROMPT,
    llm,
)

REQUIRED_FIELDS = ["forecasting_horizon"]

@traceable(name="strategy_planner")
def plan_strategy(state: Dict[str, Any]) -> Dict[str, Any]:
    parsed = state.get("parsed_problem")

    if parsed is None:
        raise ValueError("parsed_problem missing from state")

    missing = []
    for field in REQUIRED_FIELDS:
        if getattr(parsed, field) in (None, "", []):
            missing.append(field)

    if missing:
        questions = [
            f"Please specify the {field.replace('_', ' ')} for the forecasting task."
            for field in missing
        ]

        return {
            **state,
            "clarification_questions": questions
        }

    if getattr(parsed, "horizon_assumed", False):
        return {
            **state,
            "clarification_questions": [
                f"I assumed a {parsed.forecasting_horizon} forecasting horizon. "
                "Please confirm or specify a different horizon."
            ]
        }

    messages = [
        SystemMessage(content=STRATEGY_SYSTEM_PROMPT),
        HumanMessage(content=f"""
Forecasting problem:
{parsed}

Relevant modeling guidelines:
{state.get('retrieved_context')}
""")
    ]

    structured_llm = llm.with_structured_output(ModelingPlan)

    try:
        plan = structured_llm.invoke(messages)
    except Exception as e:
        raise ValueError(f"Failed to generate modeling plan: {e}")

    return {
        **state,
        "modeling_plan": plan,
        "clarification_questions": []
    }
