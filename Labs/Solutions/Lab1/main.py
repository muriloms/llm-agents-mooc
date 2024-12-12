from typing import Dict, List
from autogen import ConversableAgent, register_function
import sys
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# Constants for scoring
SCORE_KEYWORDS = {
    1: ["awful", "horrible", "disgusting"],
    2: ["bad", "unpleasant", "offensive"],
    3: ["average", "uninspiring", "forgettable"],
    4: ["good", "enjoyable", "satisfying"],
    5: ["awesome", "incredible", "amazing"]
}

# Data processing functions
def normalize(name: str) -> str:
    '''
    Normalizes restaurant name by converting to lowercase,
    replacing punctuation with space,
    and removing extra spaces

    Args:
    name (str): restaurant name to normalize

    Returns:
    str: normalized restaurant name
    '''
    return (name.lower().replace('-',' ').replace('.',' ').replace('  ',' ').strip())


def fetch_restaurant_data(restaurant_name: str) -> Dict[str, List[str]]:
    ''' 
    Fetches reviews for a specific restaurant from the data file

    Args:
    restaurant_name (str): name of the restaurant to search for

    Returns:
    Dict[str, List[str]]: dictionary with restaurant name as key and list of reviews
    '''
    # Load the restaurant data
    try:
        with open('restaurant-data.txt','r') as file:
            data = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError("The file 'restaurant-data.txt' was not found")
    
    restaurant_data = {}
    restaurant_reviews = []
    actual_name = None

    # Normalize the restaurant name
    restaurant_name_normalized = normalize(restaurant_name)

    # Parse the reviews
    for line in data:
        if not line.strip():
            continue

        # Normalize the line
        line_normalized = normalize(line)

        if line_normalized.startswith(restaurant_name_normalized):
            actual_name = line.split(".")[0].strip()
            restaurant_reviews.append(line.strip())

    # Fetch reviews for the given restaurant name
    if actual_name and restaurant_reviews:
        restaurant_data[actual_name] = restaurant_reviews
    else:
        # Return an empty list if no reviews found
        restaurant_data[actual_name] = [] 

    return restaurant_data

def calculate_overall_score(restaurant_name: str,
                            food_scores: List[str],
                            customer_service_scores: List[int]
                            ) -> Dict[str, float]:
    '''
    Calculates overall restaurant score using geometric mean formula

    Args:
    restaurant_name (str): name of the restaurant
    food_scores (List[int]): list of food quality scores (1-5)
    customer_service_scores (List[int]): list of service quality socres (1-5)

    Returns:
    Dict[str,float]: dictionary with restaurant name and calculated score
    '''
    restaurant_data = {}

    N = len(food_scores)
    if N != len(customer_service_scores) or N==0:
        raise ValueError("Food scores and customer service score must have the same non-zero length")
    
    total = sum(
        ((fs**2 * css)**0.5) * (1 / (N * (125**0.5))) * 10
        for fs, css in zip(food_scores, customer_service_scores)
    )

    formatted_score = "{:.3f}".format(total)
    restaurant_data[restaurant_name] = formatted_score

    return restaurant_data

def get_data_fetch_agent_prompt(restaurant_query: str) -> str:
    '''
    Generates a prompt for the data fetch agent to extract restaurant names
    from user queries and fetch their corresponding reviews

    Args:
    restaurant_query (str): the user's query containing the name of the restaurant

    Returns:
    struct_prompt (str): A structured prompt guiding the data fetch agent to:
        1. Analyze the user's query
        2. Extract the restaurant name.
        3. Call the 'fetch_restaurant_data' function with the extracted name
    '''
    struct_prompt = f"""You are a data fetch agent responsible for extractin restaurant names from user queries and fetch their reviews
    Your task:
    1. Analyze the user query: "{restaurant_query}"
    2. Extract the restaurant name from the query
    3. Call the fetch_restaurant_data function with the extracted name
    """
    return struct_prompt

def get_review_analyzer_prompt() -> str:
    '''
    Generates a prompt for the review analyzer agent to extract scores for
    food quality and customer service quality from restaurant reviews

    Global variables:
    SCORE_KEYWORDS (Dict[int, List[str]]): a dictionary mapping scores (1-5) to a list
    of descriptive keywords for food and customer service

    Returns:
    struct_prompt (str): a formatted string serving as the review analyzer agent's prompt
    '''
    keywords_str = "\n".join(
        f"        - {score}/5: {', '.join(words)}"
        for score, words in SCORE_KEYWORDS.items()
    )
    
    return f"""You are a review analyzer agent. Your task is to analyze restaurant reviews and extract scores.
    
    For each review:
    1. Find exactly one keyword for food quality and one for service quality
    2. Map keywords to scores using this exact mapping:
        Food/Service Score Mapping:
    
    {keywords_str}
    
    Output format must be exactly:
    food_scores = [score1, score2, ...]
    customer_service_scores = [score1, score2, ...]"""

def get_scoring_agent_prompt() -> str:
    '''
    Generates a prompt for the scoring agent tasked with calculating the final rating 
    for a restaurant based on food scores and customer service scores.

    Returns:
        str: A structured prompt for the scoring agent.
    '''
    return """You are a scoring agent. Your task is to take the food scores and customer service scores from the previous conversation and calculate the final rating.

    Steps:
    1. Extract the restaurant name from the data fetch result
    2. Get the food_scores and customer_service_scores lists from the analyzer
    3. Call calculate_overall_score with these exact parameters
    
    """

def create_agent(name: str, system_message: str, llm_config: dict) -> ConversableAgent:
    """
    Helper function to create agents with consistent configuration.

    This function initializes and returns a `ConversableAgent` instance 
    with the specified name, system message, and LLM configuration.

    Args:
        name (str): The name of the agent being created.
        system_message (str): The system-level message or prompt to initialize the agent's context.
        llm_config (dict): Configuration parameters for the large language model (LLM),
                           such as model name, temperature, max tokens, etc.

    Returns:
        ConversableAgent: An instance of the `ConversableAgent` class configured with the specified parameters.

    Example:
        agent_name = "data_fetch_agent"
        system_message = "You are a data fetch agent responsible for retrieving restaurant reviews."
        llm_config = {"model": "gpt-4", "temperature": 0.7, "max_tokens": 200}

        data_fetch_agent = create_agent(agent_name, system_message, llm_config)
    """
    agent = ConversableAgent(
        name=name,
        system_message=system_message,
        llm_config=llm_config
    )

    return agent


def main(user_query: str):
    '''
    Main function to process restaurant queries and return ratings

    Args:
    user_query (str): user's query about a restaurant

    Returns:
    The result of the agent conversation chain
    '''

    llm_config = {"config_list": [{"model": "gpt-4", "api_key": os.environ.get("OPENAI_API_KEY")}]}

    # Create the entrypoint agent
    msg_entrypoint_agent = """You are the supervisor agent coordinating the restaurant review analysis process.
    Follow these steps exactly:
    1. First, ask the data fetch agent to get restaurant reviews using fetch_restaurant_data
    2. Once you have the reviews, send them to the review analyzer to extract scores
    3. After getting the scores from the analyzer, ask the scoring agent to calculate the final rating
    """

    entrypoint_agent = create_agent(
        "entrypoint_agent",
        msg_entrypoint_agent,
        llm_config
    )

    # Create specialized agents
    agents = {
        "data_fetch": create_agent(
            "data_fetch_agent",
            get_data_fetch_agent_prompt(user_query),
            llm_config
        ),
        "analyzer": create_agent(
            "review_analyzer_agent",
            get_review_analyzer_prompt(),
            llm_config
        ),
        "scorer": create_agent(
            "scoring_agent",
            get_scoring_agent_prompt(),
            llm_config
        )
    }

    # Register functions for all necessary agents
    # Data fetch related
    register_function(
        fetch_restaurant_data,
        caller=entrypoint_agent,  
        executor=agents['data_fetch'], 
        name="fetch_restaurant_data", 
        description="Fetches the reviews for a specific restaurant."
    )
    
    # Scoring related
    register_function(
        calculate_overall_score,
        caller=entrypoint_agent,  
        executor=agents['scorer'], 
        name="calculate_overall_score", 
        description="Calculates the overall score for a restaurant."
    )
    # Update chat sequence with more explicit messages
    chat_sequence = [
        {
            "recipient": agents["data_fetch"],
            "message": f"Find reviews for this query: {user_query}",
            "summary_method": "last_msg",
            "max_turns": 2
        },
        {
            "recipient": agents["analyzer"],
            "message": "Here are the reviews from the data fetch agent. Please analyze them and extract food and service scores. For each review, find the food quality keyword and service quality keyword, then map them to scores 1-5 according to the scoring rules.",
            "summary_method": "last_msg",
            
            "max_turns": 1
        },
        {
            "recipient": agents["scorer"],
            "message": "Using the food_scores and customer_service_scores from the analyzer, please calculate the final restaurant rating using calculate_overall_score.",
            "summary_method": "last_msg",
            "max_turns": 2
        }
    ]
    
    result = entrypoint_agent.initiate_chats(chat_sequence)
    print(result)
    return result


if __name__ == "__main__":
    assert len(sys.argv) > 1, "Please ensure you include a query for some restaurant when executing main."
    main(sys.argv[1])