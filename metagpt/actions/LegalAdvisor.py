
from metagpt.roles import Role
from metagpt.schema import Message

class LegalAdvisor(Role):
    role = "LegalAdvisor"

    async def perform(self, message: Message):
        if message.content == "Initial Legal Review":
            print("Conducting initial legal review for the startup.")
        elif message.content == "Contract Review":
            print("Reviewing the contract before finalizing.")
        else:
            print(f"Handling other legal matters: {message.content}")
