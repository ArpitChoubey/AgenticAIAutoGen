import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient




async def main():
    model_client = OpenAIChatCompletionClient( model="gpt-4o" )

    assistant = AssistantAgent( name="biology Tutor", model_client=model_client,
                                system_message="You are helpful biology tutor.Help the user solve biology problems step by step"
                                               "When the user says 'THANKS DONE' or similar, acknowledge and say 'LESSON COMPLETE' to end session." )

    user_proxy = UserProxyAgent( name="Student" )

    team = RoundRobinGroupChat( participants=[user_proxy, assistant],
                                termination_condition=TextMentionTermination( "LESSON COMPLETE" ) )
    await Console(team.run_stream(task = "I need help with more about plants and photosynthesis"))


asyncio.run( main() )


#Human - Agent-(save)  ,Agent2 (save)
