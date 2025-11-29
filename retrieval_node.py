"""
retrieval_node.py

LangGraph-compatible node for injecting domain knowledge
using semantic retrieval (RAG).
"""

from typing import Dict, Any, List
from pathlib import Path

from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langsmith import traceable


def load_documents() -> List[Document]:
    """
    Load all markdown files from the docs directory
    as LangChain Document objects.
    """
    docs_path = Path("docs")
    documents = []

    for file in docs_path.glob("*.md"):
        content = file.read_text()
        documents.append(
            Document(
                page_content=content,
                metadata={"source": file.name}
            )
        )

    return documents


documents = load_documents()
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents, embeddings)


@traceable(name="retrieve_modeling_guidelines")
def retrieve_modeling_guidelines(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Retrieve modeling guidelines relevant to the
    parsed forecasting problem.
    """

    if "parsed_problem" not in state:
        raise ValueError("State must contain `parsed_problem`.")

    query = state["parsed_problem"].target_variable

    retrieved_docs = vectorstore.similarity_search(
        query=query,
        k=3
    )

    return {
        **state,
        "retrieved_context": [
            {
                "content": doc.page_content,
                "source": doc.metadata["source"]
            }
            for doc in retrieved_docs
        ]
    }