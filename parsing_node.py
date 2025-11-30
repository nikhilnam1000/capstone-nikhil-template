"""
parsing_node.py

LangGraph-compatible node for parsing a natural language
financial forecasting problem into a structured ForecastProblem.
"""

from typing import Dict, Any

from langchain_core.messages import SystemMessage, HumanMessage
from langsmith import traceable

from llm_setup import (
    ForecastProblem,
    PROBLEM_PARSER_SYSTEM_PROMPT,
    llm,
)

@traceable(name="parse_forecasting_problem")
def parse_forecasting_problem(state: Dict[str, Any]) -> Dict[str, Any]:
    if "user_query" not in state:
        raise ValueError("State must contain `user_query`.")

    messages = [
        SystemMessage(content=PROBLEM_PARSER_SYSTEM_PROMPT),
        HumanMessage(content=state["user_query"]),
    ]

    structured_llm = llm.with_structured_output(ForecastProblem)

    try:
        parsed_problem = structured_llm.invoke(messages)
    except Exception as e:
        raise ValueError(
            f"Failed to parse forecasting problem: {e}"
        )

    return {
        **state,
        "parsed_problem": parsed_problem
    }