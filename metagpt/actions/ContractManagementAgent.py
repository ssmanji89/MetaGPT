
from metagpt.agents import Agent
from metagpt.schema import Message

class ContractManagementAgent(Agent):
    agent = "ContractManagementAgent"

    async def perform(self, message: Message):
        if message.content == "Contract Management":
            print("Managing the contracts with clients, vendors, and employees.")
        else:
            print(f"Handling other contract management matters: {message.content}")
