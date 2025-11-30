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

class ForecastGraphState(TypedDict):
    """
    Shared state across LangGraph nodes.
    """
    user_query: str
    parsed_problem: Optional[Any]
    retrieved_context: Optional[List[Dict[str, Any]]]


graph_builder = StateGraph(ForecastGraphState)

graph_builder.add_node(
    "parse_problem",
    parse_forecasting_problem
)

graph_builder.add_node(
    "retrieve_knowledge",
    retrieve_modeling_guidelines
)

graph_builder.set_entry_point("parse_problem")

graph_builder.add_edge(
    "parse_problem",
    "retrieve_knowledge"
)

graph_builder.add_edge(
    "retrieve_knowledge",
    END
)

graph = graph_builder.compile()


if __name__ == "__main__":
    initial_state = {
        "user_query": "Forecast monthly inflation for India using macroeconomic data."
    }

    final_state = graph.invoke(initial_state)

    print("FINAL STATE:")
    pprint(final_state)