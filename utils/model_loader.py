# utils/model_loader.py
import os
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field, ConfigDict

from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
# from langchain_huggingface import HuggingFaceEmbeddings  # Uncomment when you actually use it


class ModelLoader(BaseModel):
    # Which provider to use
    model_provider: Literal["openai", "groq"] = "groq"

    # Keep raw config dict (loaded once), exclude from model serialization
    config: dict[str, Any] = Field(default_factory=load_config, exclude=True)

    # Pydantic v2-style config
    model_config = ConfigDict(arbitrary_types_allowed=True)

    # Called after the model is created (Pydantic v2)
    def model_post_init(self, __context: Any) -> None:
        # Ensure .env is loaded so os.getenv works during runtime
        load_dotenv()

    def load_llm(self):
        """
        Load the LLM client for the selected provider, using values from config + env.
        Raises a clear error if required settings are missing.
        """
        provider = self.model_provider
        cfg = self.config

        if provider == "groq":
            api_key = os.getenv("GROQ_API_KEY")
            if not api_key:
                raise ValueError("GROQ_API_KEY is not set. Add it to your environment or .env.")
            try:
                model_name = cfg["llm"]["groq"]["model_name"]
            except KeyError as e:
                raise KeyError("Missing config key llm.groq.model_name in your config") from e
            return ChatGroq(model=model_name, api_key=api_key)

        if provider == "openai":
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OPENAI_API_KEY is not set. Add it to your environment or .env.")
            try:
                model_name = cfg["llm"]["openai"]["model_name"]
            except KeyError as e:
                raise KeyError("Missing config key llm.openai.model_name in your config") from e
            return ChatOpenAI(model=model_name, api_key=api_key)

        # Unknown provider
        raise ValueError(f"Unknown model_provider: {provider!r}. Expected 'openai' or 'groq'.")
