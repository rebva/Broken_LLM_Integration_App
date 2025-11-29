from langchain_community.llms import Ollama

from .settings import settings


# Create ChatGPT model for chat.
def create_chat_openai_model():
    # Only local Ollama is supported for now; cloud OpenAI is disabled.
    return Ollama(
        base_url=settings.OLLAMA_BASE_URL,
        model=settings.OLLAMA_MODEL_NAME,
        verbose=settings.OLLAMA_VERBOSE
    )
