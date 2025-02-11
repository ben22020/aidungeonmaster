import configparser
from langchain_anthropic import ChatAnthropic
from backend.database import vector_db
from dotenv import load_dotenv
import os

def create_model():
    load_dotenv()
    model = 'claude-3-5-sonnet-20240620'
    api_key = os.getenv("ANTHROPIC_API_KEY")
    max_tokens = 1024
    llm = ChatAnthropic(model = model, api_key = api_key, max_tokens = max_tokens)
    return  llm

def generate_world_history(theme:str, character_name: str, character_description: str):
    """ Generates a world history and stores key events in the vector database for future retrieval"""
    llm = create_model()
    prompt = f"""

        Generate a brief world history of a world with a {theme} theme. The goal is to lead to a natural starting point for an adventure. Tailor
        the history to be relevant to someone with the following description: {character_description}
        The world history should end with:
        Now, the protagonist {character_name} must find their way in this world. What will they do?
        """

    response = llm.invoke(prompt)
    world_history = response.content

    events = extract_events(world_history)
    for event in events:
        vector_db.store_world_memory(event)

    return world_history
    

def extract_events(input: str):
    """Extract key events from text"""
    events = input.split(". ")  
    return [event.strip() for event in events if len(event) > 10]