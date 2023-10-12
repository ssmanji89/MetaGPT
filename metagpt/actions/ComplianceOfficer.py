
from metagpt.roles import Role
from metagpt.schema import Message

class ComplianceOfficer(Role):
    role = "ComplianceOfficer"

    async def perform(self, message: Message):
        if message.content == "Initial Compliance Check":
            print("Conducting an initial compliance check for the startup.")
        elif message.content == "Periodic Compliance Audit":
            print("Conducting a periodic compliance audit.")
        elif message.content == "Tech Compliance Validation":
            print("Validating the compliance of the tech stack.")
        else:
            print(f"Handling other compliance matters: {message.content}")
