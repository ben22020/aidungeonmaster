import configparser
from langchain_anthropic import ChatAnthropic


def create_model():
    model = 'claude-3-5-sonnet-20240620'
    api_key = ""
    max_tokens = 1024
    llm = ChatAnthropic(model = model, api_key = api_key, max_tokens = max_tokens)
    return  llm

def generate_world_history(theme:str, character_name: str, character_description: str):
    llm = create_model()
    prompt = f"""

    Generate a brief world history of a world with a {theme} theme. The goal is to lead to a natural starting point for an adventure. Tailor
    the history to be relevant to someone with the following description: {character_description}
    The world history should end with:
    Now, the protagonist {character_name} must find their way in this world. What will they do?
    """

    response = llm.invoke(prompt)
    return response.content