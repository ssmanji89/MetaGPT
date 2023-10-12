
from metagpt.agents import Agent
from metagpt.schema import Message

class RegulatoryAgent(Agent):
    agent = "RegulatoryAgent"

    async def perform(self, message: Message):
        if message.content == "Update on Regulatory Changes":
            print("Updating the team about recent changes in regulations.")
        else:
            print(f"Handling other regulatory matters: {message.content}")
