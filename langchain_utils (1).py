# langchain_app/langchain_utils.py
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType
import os
from pydantic import BaseModel


os.environ['OPENAI_API_KEY'] = "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"
# gpt_key = "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"
class Message(BaseModel):
    content: str
    
class LangchainUtils:
    def __init__(self):
        # Load environment variable for OpenAI API key
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        if not self.openai_api_key:
            raise EnvironmentError("OPENAI_API_KEY environment variable not set")

        # Initialize the SQL database and toolkit
        self.db = SQLDatabase.from_uri("sqlite:///fashion_db.sqlite")
        self.toolkit = SQLDatabaseToolkit(db=self.db, llm=OpenAI(temperature=0))

        # Create agent executor
        self.agent_executor = create_sql_agent(
            llm=OpenAI(temperature=0.1),
            toolkit=self.toolkit,
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
        )
    
    def run_query(self, query: str):
        try:
            result = self.agent_executor.run(query)
            return result
        except Exception as e:
            return str(e)
