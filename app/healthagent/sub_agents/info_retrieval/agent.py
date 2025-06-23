from google.adk.agents import Agent
import datetime
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from google.genai import types # For Content/Part types if needed for advanced instruction templates

# --- Tool Definitions (Mock Implementations) ---
def perform_search(query: str) -> dict:
    """
    Performs a simulated web search for the given query.
    Args:
        query (str): The search query.
    Returns:
        dict: A dictionary with 'status' ('success' or 'no_results') and 'results'.
    """
    print(f"--- Tool: perform_search called with query: '{query}' ---")
    if "capital of australia" in query.lower():
        return {"status": "success", "results": "Canberra is the capital city of Australia."}
    elif "latest ai news" in query.lower():
        return {"status": "success", "results": "Latest AI news: Advancements in generative models continue to impress, with new breakthroughs in multimodal AI."}
    else:
        return {"status": "no_results", "results": "No relevant information found."}

def retrieve_document_content(document_name: str, query: str) -> dict:
    """
    Retrieves content from a simulated internal document.
    Args:
        document_name (str): The name of the document (e.g., "HR_Policy_2024.pdf").
        query (str): The specific information to retrieve from the document.
    Returns:
        dict: A dictionary with 'status' ('success', 'not_found', 'error') and 'content'.
    """
    print(f"--- Tool: retrieve_document_content called for '{document_name}' with query: '{query}' ---")
    if document_name.lower() == "hr_policy_2024.pdf" and "vacation days" in query.lower():
        return {"status": "success", "content": "The HR_Policy_2024.pdf states that employees are eligible for 15 vacation days per year, plus public holidays."}
    elif document_name.lower() == "security_guide.docx" and "incident response" in query.lower():
        return {"status": "success", "content": "The Security_Guide.docx outlines a 3-step incident response plan: identify, contain, and recover."}
    elif document_name.lower() == "hr_policy_2024.pdf":
        return {"status": "not_found", "content": f"Information about '{query}' not found in 'HR_Policy_2024.pdf'."}
    else:
        return {"status": "error", "content": f"Document '{document_name}' not accessible or does not exist."}

# --- Import Instructions from instructions.py ---
from info_retrieval.instructions import INFO_RETRIEVAL_INSTRUCTIONS

# --- Agent Definition ---
info_retrieval_agent = Agent(
    name="info_retrieval_agent",
    model="gemini-2.0-flash", # Using a common model [8, 9]
    description="Specialized agent for retrieving factual information from general searches and specific documents.",
    instruction=instructions.INFO_RETRIEVAL_INSTRUCTIONS,
    tools=[
        FunctionTool(perform_search),
        FunctionTool(retrieve_document_content)
    ]
)
