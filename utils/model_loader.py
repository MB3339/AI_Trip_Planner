import os
from dotenv import load_dotenv
from typing import literal,Optional,Any
from pydantic import BaseModel, Field
from langchain_huggingface import HuggingfaceEmbeddings
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI


from typing_extensions import Any


class configLoader():
    def __init__(self):
        pass

def __getitem__(self,key):
    return self.config[key]



class ModelLoader(BaseModel):
    model_provider: Literal['openai', 'groq']= 'groq'
    config:Optional[configLoader]=Field(default=None,exclude=True)

    def model_post_init(self, __context: Any)-> None:
        self.config= configLoader()

    class Config:
        arbitrary_types_allowed = True

    def load_llm(self):
        """
        Load the LLM model based on the configuration.
        """
        print("LLM loading........")
        print(f"Loading model for provider : {self.model_provider}")
        if self.model_provider == 'groq':
            print("loading LLM from Groq......")
            groq_api_key=os.getenv("GROQ_API_KEY")
            model_name = self.config['llm']['groq']['model_name']
            llm=ChatGroq(model=model_name, api_key=groq_api_key)
        
        elif self.model_provider == 'openai':
            print("loading LLM from OpenAI......")
            openai_api_key=os.getenv("OPENAI_API_KEY")
            model_name = self.config['llm']['openai']['model_name']
            llm=ChatOpenAI(model=model_name, api_key=openai_api_key)

        return llm