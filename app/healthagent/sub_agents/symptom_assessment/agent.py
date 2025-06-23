from google.adk.agents import Agent
from google.adk.tools import FunctionTool

# --- Tool Definitions (Mock Implementations) ---
def lookup_symptom_info(symptom: str) -> dict:
    """
    Looks up general information about a health symptom.
    Args:
        symptom (str): The symptom described by the user.
    Returns:
        dict: A dictionary with 'status' ('success' or 'no_info') and 'info'.
    """
    print(f"--- Tool: lookup_symptom_info called for symptom: '{symptom}' ---")
    symptom = symptom.lower()
    if "headache" in symptom:
        return {"status": "success", "info": "Headaches are common and can stem from stress, dehydration, or fatigue. Most are mild but severe ones can indicate other issues."}
    elif "fever" in symptom:
        return {"status": "success", "info": "Fever is an elevated body temperature, often a sign of infection. It can be accompanied by chills and sweating."}
    elif "chest pain" in symptom or "dizzy" in symptom:
        return {"status": "success", "info": "Chest pain and dizziness can be signs of serious underlying conditions and should be evaluated by a medical professional immediately."}
    else:
        return {"status": "no_info", "info": "No general information found for this specific symptom."}

def suggest_general_next_steps(symptom: str) -> dict:
    """
    Suggests general, non-medical next steps based on a symptom.
    Args:
        symptom (str): The symptom for which to suggest next steps.
    Returns:
        dict: A dictionary with 'status' ('success') and 'recommendation'.
    """
    print(f"--- Tool: suggest_general_next_steps called for symptom: '{symptom}' ---")
    symptom = symptom.lower()
    if "chest pain" in symptom or "dizzy" in symptom or "shortness of breath" in symptom:
        return {"status": "success", "recommendation": "Seek immediate medical attention or call emergency services for these symptoms."}
    elif "headache" in symptom or "fever" in symptom:
        return {"status": "success", "recommendation": "Consider resting, staying hydrated, and if symptoms persist or worsen, consult a healthcare professional."}
    else:
        return {"status": "success", "recommendation": "Monitor your symptoms, and if you are concerned or they worsen, please consult a healthcare professional."}

# --- Import Instructions from instructions.py ---
import instructions

# --- Agent Definition ---
symptom_assessment_agent = Agent(
    name="symptom_assessment_agent",
    model="gemini-2.0-flash", # Using a common model [8, 9]
    description="Provides general, non-diagnostic information about health symptoms and recommends appropriate next steps.",
    instruction=instructions.SYMPTOM_ASSESSMENT_INSTRUCTIONS,
    tools=[
        FunctionTool(lookup_symptom_info),
        FunctionTool(suggest_general_next_steps)
    ]
)