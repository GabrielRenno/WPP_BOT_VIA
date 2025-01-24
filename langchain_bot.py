# langchain_bot.py
import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize the ChatOpenAI model (using GPT-3.5 or GPT-4, whichever you have access to)
llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.7  # Adjust temperature for creativity vs. consistency
)

# Use a conversation buffer memory to track context across messages
memory = ConversationBufferMemory()

# Create a conversation chain
conversation = ConversationChain(
    llm=llm,
    verbose=False,
    memory=memory
)

def get_answer(message):
    """
    Passes the user's message to the LangChain conversation 
    and returns the LLM's response.
    """
    response = conversation.run(input=message)
    return response
