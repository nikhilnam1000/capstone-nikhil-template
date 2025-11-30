Template for creating and submitting MAT496 capstone project.

# Overview of MAT496

In this course, we have primarily learned Langgraph. This is helpful tool to build apps which can process unstructured `text`, find information we are looking for, and present the format we choose. Some specific topics we have covered are:

- Prompting
- Structured Output 
- Semantic Search
- Retrieval Augmented Generation (RAG)
- Tool calling LLMs & MCP
- Langgraph: State, Nodes, Graph

We also learned that Langsmith is a nice tool for debugging Langgraph codes.

------

# Capstone Project objective

The first purpose of the capstone project is to give a chance to revise all the major above listed topics. The second purpose of the capstone is to show your creativity. Think about all the problems which you can not have solved earlier, but are not possible to solve with the concepts learned in this course. For example, We can use LLM to analyse all kinds of news: sports news, financial news, political news. Another example, we can use LLMs to build a legal assistant. Pretty much anything which requires lots of reading, can be outsourced to LLMs. Let your imagination run free.


-------------------------

# Project Report 

## Title: Financial Forecasting Strategy Assistant

## Overview

This project implements a financial forecasting strategy assistant using LangGraph and LangChain.
Given a natural language forecasting problem (e.g. inflation forecasting, stock return prediction, volatility modeling), the assistant proposes a detailed modeling strategy rather than performing numerical forecasts.
The assistant:
1. Interprets the forecasting objective
2. Suggests appropriate modeling approaches (regression, time-series, machine learning, neural networks)
3. Specifies data requirements and preprocessing steps
4. Explains feature engineering, regularization, and evaluation metrics
5. Provides interpretation guidelines
6. Supports follow-up analytical questions
7. The system emphasizes structured reasoning, traceability, and modular design, making it suitable for complex analytical workflows.

## Reason for picking up this project

+ This project is designed to revise and apply the key concepts taught in MAT496:
+ Prompting structured output using schema-based responses
+ LangGraph for multi-step reasoning with explicit state and nodes
+ Tool-based LLM usage for controllable analysis 
+ LangSmith for tracing and debugging LLM-driven pipelines
+ Retrieval-Augmented Generation (RAG) for injecting domain knowledge
+ Semantic search over modeling guidelines
+ Financial forecasting problems are inherently unstructured and multi-step, making them well-suited for LangGraph-based approaches.

## Plan

I plan to execute these steps to complete my project.

[DONE] Step 1: Initialize LLM, LangSmith tracing, and structured output schemas
+ Configure the LLM with finance-appropriate parameters
+ Enable LangSmith tracing for debugging and inspection 
+ Define structured output schemas for forecasting problems and modeling plans
+ Centralize configuration to be reused across all LangGraph nodes

[DONE] Step 2: Problem parsing and intent extraction 
+ Extract forecasting target, horizon, frequency, and constraints from user input

[DONE] Step 3: Semantic retrieval and RAG integration 
+ Retrieve relevant modeling guidelines using semantic search

[DONE] Step 4: LangGraph workflow construction
+ Define graph state, nodes, and transitions

[DONE] Step 5: Strategy validation and synthesis 
+ Validate model assumptions and synthesize final recommendations

[DONE] Step 6: External context augmentation using Tavily Search

[DONE] Step 7: Streamlit application for interactive usage 
+ Build a simple user-facing interface

Video Link: https://drive.google.com/drive/u/0/folders/11mRv8pqEV7xlpcLMZbiGmnLrDenTIybdç

## Conclusion:

I had planned to achieve building a model that takes a particular situation, analyses it and tells the user the best way to go on about building a model and all the things to keep in mind to execute. I think I have scratched the surface of this problem statement, but I believe it needs a lot more detail and more concrete explanations. 

----------

# Added instructions:

- This is a `solo assignment`. Each of you will work alone. You are free to talk, discuss with chatgpt, but you are responsible for what you submit. Some students may be called for viva. You should be able to each and every line of work submitted by you.

- `commit` History maintenance.
  - Fork this repository and build on top of that.
  - For every step in your plan, there has to be a commit.
  - Change [TODO] to [DONE] in the plan, before you commit after that step. 
  - The commit history should show decent amount of work spread into minimum two dates. 
  - **All the commits done in one day will be rejected**. Even if you are capable of doing the whole thing in one day, refine it in two days.  
 
 - Deadline: Nov 30, Sunday 11:59 pm


# Grading: total 25 marks

- Coverage of most of topics in this class: 20
- Creativity: 5
  