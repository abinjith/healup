from google.adk.agents import Agent
from google.adk.tools import FunctionTool

# --- Tool Definitions (Mock Implementations) ---
def suggest_support_resources(reason: str) -> dict:
    """
    Provides contact information for general emotional support or crisis resources.
    Args:
        reason (str): The reason for needing support (e.g., "feeling overwhelmed", "crisis").
    Returns:
        dict: A dictionary with 'status' ('success') and 'resources'.
    """
    print(f"--- Tool: suggest_support_resources called for reason: '{reason}' ---")
    reason_lower = reason.lower()
    if "crisis" in reason_lower or "harm" in reason_lower or "suicidal" in reason_lower:
        return {
            "status": "success",
            "resources": """
            If you are in immediate danger or experiencing a mental health crisis, please reach out for professional help right away:
            - **National Crisis and Suicide Lifeline**: Call or text 988 (available 24/7 in the US).
            - **Emergency Services**: Call 911 (or your local emergency number).
            - **Local Mental Health Services**: Search online for local mental health crisis centers.
            Please connect with these resources immediately.
            """
        }
    else:
        return {
            "status": "success",
            "resources": """
            It's brave to seek support. Here are some general resources that can offer a listening ear and guidance:
            - **NAMI (National Alliance on Mental Illness)** Helpline: 1-800-950-NAMI (6264)
            - **Crisis Text Line**: Text HOME to 741741
            - **Your local mental health services**: Consider searching for therapists or counselors in your area for personalized support.
            Connecting with a human professional can provide the in-depth support you might need.
            """
        }

def provide_coping_strategies(topic: str) -> dict:
    """
    Offers general, non-clinical coping strategies for common emotional states.
    Args:
        topic (str): The emotional state or challenge (e.g., "stress", "loneliness").
    Returns:
        dict: A dictionary with 'status' ('success') and 'strategies'.
    """
    print(f"--- Tool: provide_coping_strategies called for topic: '{topic}' ---")
    topic_lower = topic.lower()
    if "stress" in topic_lower or "anxiety" in topic_lower:
        return {
            "status": "success",
            "strategies": """
            For managing stress or anxiety, consider:
            - Deep breathing exercises: Inhale slowly through your nose, hold, and exhale slowly through your mouth.
            - Short breaks: Step away from your tasks for a few minutes to clear your head.
            - Light physical activity: Even a short walk can help.
            - Mindful moments: Focus on your senses (what you see, hear, smell, touch, taste) to stay present.
            """
        }
    elif "loneliness" in topic_lower or "sadness" in topic_lower:
        return {
            "status": "success",
            "strategies": """
            If you're feeling lonely or sad, you might try:
            - Reaching out to a trusted friend or family member.
            - Engaging in a hobby or activity you enjoy.
            - Spending time in nature.
            - Practicing self-compassion.
            """
        }
    else:
        return {
            "status": "success",
            "strategies": "Focus on self-care, reach out to trusted individuals, and consider seeking professional guidance if feelings persist."
        }

# --- Import Instructions from instructions.py ---
import instructions

# --- Agent Definition ---
emotional_support_agent = Agent(
    name="emotional_support_agent",
    model="gemini-2.0-flash", # Using a common model [8, 9]
    description="Provides empathetic emotional support and guides users to professional resources.",
    instruction=instructions.EMOTIONAL_SUPPORT_INSTRUCTIONS,
    tools=[
        FunctionTool(suggest_support_resources),
        FunctionTool(provide_coping_strategies)
    ]
)
