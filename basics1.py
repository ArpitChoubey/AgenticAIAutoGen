import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient



async def main1():
    print( "I am inside function" )

    model_client = OpenAIChatCompletionClient(
        model="gpt-4o" )
    assistant = AssistantAgent( name="assistant", model_client=model_client )
    await Console( assistant.run_stream( task="What is 25 * 9?" ) )
    await model_client.close()


asyncio.run( main1() )
