import os
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.prompts import PromptTemplate

class OfflineLLMConnector:
    """
    Handles connections to local, offline inference servers (e.g., Ollama).
    """

    def __init__(self, chat_model: str = "llama3", embed_model: str = "all-minilm"):
        self.chat_model = chat_model
        self.embed_model = embed_model
        # Docker needs host.docker.internal to talk to Windows Ollama
        self.base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self._llm = None
        self._embeddings = None

    @property
    def llm(self) -> ChatOllama:
        """
        Lazy-loads the Ollama Chat Model
        """
        if not self._llm:
            self._llm = ChatOllama(
                model=self.chat_model,
                base_url=self.base_url,
                temperature=0.1,  # Low temperature for strict routing logic
                format="json"     # We enforce JSON output for Pydantic parsing
            )
        return self._llm

    @property
    def embeddings(self) -> OllamaEmbeddings:
        """
        Lazy-loads the Ollama Embedding Model
        """
        if not self._embeddings:
            self._embeddings = OllamaEmbeddings(
                model=self.embed_model,
                base_url=self.base_url
            )
        return self._embeddings

    def generate_routing_decision(self, prompt_text: str):
        """
        Placeholder method to invoke the LLM for routing
        """
        return self.llm.invoke(prompt_text)

# Singleton instance for the application to import
offline_llm = OfflineLLMConnector(chat_model="llama3")
