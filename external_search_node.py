"""
external_search_node.py

LangGraph node for augmenting the modeling plan
with external, up-to-date context using Tavily.
"""

from typing import Dict, Any

from langsmith import traceable
from langchain_community.tools.tavily_search import TavilySearchResults


@traceable(name="external_context_search")
def external_context_search(state: Dict[str, Any]) -> Dict[str, Any]:
    plan = state.get("modeling_plan")

    # If no plan exists (clarifications pending), do nothing
    if plan is None:
        return state

    search_queries = [
        "India inflation data source",
        "RBI macroeconomic data",
        "MOSPI CPI India inflation",
    ]

    tavily = TavilySearchResults(max_results=3)

    results = []
    for q in search_queries:
        results.extend(tavily.invoke(q))

    return {
        **state,
        "external_context": results
    }