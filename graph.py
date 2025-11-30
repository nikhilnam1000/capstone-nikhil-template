"""
graph.py

Defines the LangGraph workflow for the
financial forecasting strategy assistant.
"""

from typing import TypedDict, Optional, List, Dict, Any

from langgraph.graph import StateGraph, END

from parsing_node import parse_forecasting_problem
from retrieval_node import retrieve_modeling_guidelines
from pprint import pprint
from strategy_node import plan_strategy
from external_search_node import external_context_search

def append_list_reducer(old, new):
    if old is None:
        return new
    if new is None:
        return old
    return old + new

class ForecastGraphState(TypedDict):
    """
    Shared state across LangGraph nodes.
    """
    user_query: str
    parsed_problem: Optional[Any]
    retrieved_context: Optional[List[Dict[str, Any]]]
    modeling_plan: Optional[Dict[str, Any]]
    clarification_questions: Optional[List[str]]
    external_context: Optional[list[dict]]

graph_builder = StateGraph(
    ForecastGraphState,
    reducers={
        "clarification_questions": append_list_reducer
    }
)

graph_builder.add_node("parse_problem", parse_forecasting_problem)
graph_builder.add_node("retrieve_knowledge", retrieve_modeling_guidelines)
graph_builder.add_node("plan_strategy", plan_strategy)
graph_builder.add_node("external_search", external_context_search)

graph_builder.set_entry_point("parse_problem")

graph_builder.add_edge("parse_problem","retrieve_knowledge")
graph_builder.add_edge("retrieve_knowledge", "plan_strategy")
graph_builder.add_edge("plan_strategy", "external_search")
graph_builder.add_edge("external_search", END)

graph = graph_builder.compile()


if __name__ == "__main__":
    initial_state = {
        "user_query": "Forecast monthly inflation for India using macroeconomic data."
    }

    final_state = graph.invoke(initial_state)

    print("FINAL STATE:")
    pprint(final_state)