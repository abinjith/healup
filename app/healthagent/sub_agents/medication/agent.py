from google.adk.agents import Agent
from google.adk.tools import FunctionTool

# --- Tool Definitions (Mock Implementations) ---
def get_medication_details(medication_name: str) -> dict:
    """
    Retrieves simulated details for a specified medication.
    Args:
        medication_name (str): The name of the medication.
    Returns:
        dict: A dictionary with medication details, 'status' ('success', 'not_found', 'error').
    """
    print(f"--- Tool: get_medication_details called for medication: '{medication_name}' ---")
    medication_name_lower = medication_name.lower()
    if medication_name_lower == "aspirin":
        return {
            "status": "success",
            "name": "Aspirin",
            "uses": "Pain relief, fever reduction, anti-inflammatory.",
            "side_effects": "Upset stomach, heartburn, nausea, mild bleeding.",
            "warnings": "Do not use if allergic, or if you have a history of bleeding disorders. Consult doctor for children with flu-like symptoms.",
            "dosage": "Typical adult dosage for pain: 325-650 mg every 4-6 hours as needed."
        }
    elif medication_name_lower == "lisinopril":
        return {
            "status": "success",
            "name": "Lisinopril",
            "uses": "Treats high blood pressure and heart failure.",
            "side_effects": "Dizziness, lightheadedness, dry cough, fatigue.",
            "warnings": "May cause kidney problems or high potassium. Avoid during pregnancy. Consult doctor before use.",
            "dosage": "Typical adult dosage for hypertension: 10-40 mg once daily."
        }
    elif medication_name_lower == "ibuprofen":
        return {
            "status": "success",
            "name": "Ibuprofen",
            "uses": "Pain relief, fever reduction, anti-inflammatory.",
            "side_effects": "Stomach upset, nausea, headache.",
            "warnings": "May increase risk of heart attack or stroke. Avoid with stomach ulcers. Consult doctor before use.",
            "dosage": "Typical adult dosage for pain: 200-400 mg every 4-6 hours as needed."
        }
    else:
        return {"status": "not_found", "message": f"Information for '{medication_name}' not found in our database."}

# --- Import Instructions from instructions.py ---
from medication_info.instructions import MEDICATION_INFO_INSTRUCTIONS

# --- Agent Definition ---
medication_info_agent = Agent(
    name="medication_info_agent",
    model="gemini-2.0-flash", # Using a common model [8, 9]
    description="Provides factual information about medications, including uses, side effects, and warnings.",
    instruction=instructions.MEDICATION_INFO_INSTRUCTIONS,
    tools=[
        FunctionTool(get_medication_details)
    ]
)