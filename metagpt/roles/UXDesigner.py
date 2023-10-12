
# User Experience (UX) Designer Role for MetaGPT Project

from metagpt.actions import Action
from metagpt.roles import Role
from metagpt.schema import Message

class CreateMockups(Action):

    PROMPT_TEMPLATE = "Create mockups for the following user interface requirements:\n{requirements}"

    async def run(self, requirements: str):
        # Here, you could integrate a design tool or simply generate a design specification
        mockups = "Generated mockups will be here"
        return mockups

class UserTesting(Action):

    PROMPT_TEMPLATE = "Run user testing based on the following criteria:\n{criteria}"

    async def run(self, criteria: str):
        # Here, you could run user tests and generate results
        testing_results = "User testing results will be here"
        return testing_results

class UXDesigner(Role):

    def __init__(
        self,
        name: str = "UXDesigner",
        profile: str = "UXDesigner",
        **kwargs,
    ):
        super().__init__(name, profile, **kwargs)
        self._init_actions([CreateMockups, UserTesting])

    async def _act(self) -> Message:
        todo = self._rc.todo
        msg = self._rc.memory.get()[-1]

        if isinstance(todo, CreateMockups):
            requirements = msg.content
            result = await CreateMockups().run(requirements)

        elif isinstance(todo, UserTesting):
            criteria = msg.content
            result = await UserTesting().run(criteria)

        return Message(content=result, role=self.profile, cause_by=todo)
