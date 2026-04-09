from tools import *
from groq import Groq

client = Groq(api_key="YOUR_GROQ_API_KEY")

def run_agent(user_input):

    # Simple intent detection
    if "log" in user_input.lower():
        return log_interaction(user_input)

    elif "edit" in user_input.lower():
        return edit_interaction(user_input)

    elif "hcp" in user_input.lower():
        return get_hcp_data(user_input)

    elif "schedule" in user_input.lower():
        return schedule_meeting(user_input)

    else:
        return generate_summary(user_input)