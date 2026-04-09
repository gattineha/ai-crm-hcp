import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from database import SessionLocal, Interaction

load_dotenv()

# Initialize LLM once globally to avoid repeated creation
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

def run_agent(user_input):
    """
    Send user input to the LLM and return the response.
    """
    # Optional: You can store logs in DB
    db = SessionLocal()
    interaction = Interaction(
        doctor="Dr. Sharma",
        topic=user_input,
        outcome="Pending"
    )
    db.add(interaction)
    db.commit()
    db.close()

    # Get AI response
    response = llm.invoke(user_input)
    return response.content