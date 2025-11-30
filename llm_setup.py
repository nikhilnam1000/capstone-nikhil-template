"""
llm_setup.py

Centralized configuration for:
- LLM initialization
- LangSmith tracing
- Structured output schemas

This module is imported by all LangGraph nodes to ensure
consistent configuration and traceability.
"""
import os
from typing import List, Optional

from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langsmith import traceable
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGSMITH_PROJECT"] = "financial-forecast-assistant"
os.environ["LANGSMITH_TRACING"] = "true"


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    max_tokens=1200,
)

class ForecastProblem(BaseModel):
    """
    Structured representation of a forecasting problem extracted
    from user input.
    """
    target_variable: str
    forecasting_horizon: Optional[str]
    data_frequency: Optional[str]
    domain: str
    constraints: Optional[List[str]]

class ModelingPlan(BaseModel):
    """
    Structured modeling strategy proposed by the assistant.
    """
    recommended_models: List[str]
    data_requirements: List[str]
    preprocessing_steps: List[str]
    feature_engineering: List[str]
    regularization_strategy: Optional[str]
    evaluation_metrics: List[str]
    interpretation_guidelines: List[str]

PROBLEM_PARSER_SYSTEM_PROMPT = """
You are a financial modeling expert.
Extract forecasting problem details precisely.
Return output strictly in the specified schema.
"""

STRATEGY_SYSTEM_PROMPT = """
You are a quantitative finance advisor.
Propose modeling strategies, not predictions.
Do not provide numerical forecasts or trading advice.
"""

@traceable(name="base_llm_call")
def invoke_llm(messages):
    """
    Wrapper around the LLM invocation to ensure LangSmith tracing.
    """
    return llm.invoke(messages)

