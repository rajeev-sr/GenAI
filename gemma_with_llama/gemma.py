from llama_index.llms.ollama import Ollama
# from llama_index.core.llms.types import Message

# Set up Ollama LLM instance
llm = Ollama(
    model="gemma:2b",  # your model name
    base_url="http://localhost:11434"
)

# Use Message objects instead of dicts
# messages = [Message(role="user", content="Who is Virat Kohli?")]

# Query the model
# response = llm.chat(messages=messages)

# Print response
# print(response.message.content)
