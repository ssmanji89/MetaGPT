
# TestGenerationAgent for MetaGPT Project

from metagpt.actions import Action
from metagpt.roles import Role
from metagpt.schema import Message

class GenerateUnitTests(Action):

    PROMPT_TEMPLATE = "Generate unit tests for the following Python function:\n{code}"

    async def run(self, code: str):
        prompt = self.PROMPT_TEMPLATE.format(code=code)
        rsp = await self._aask(prompt)
        return rsp

class RunTests(Action):

    PROMPT_TEMPLATE = "Execute the following unit tests and generate a report:\n{tests}"

    async def run(self, tests: str):
        prompt = self.PROMPT_TEMPLATE.format(tests=tests)
        rsp = await self._aask(prompt)
        return rsp

class TestGenerationAgent(Role):

    def __init__(
        self,
        name: str = "TestGen",
        profile: str = "TestGenerationAgent",
        **kwargs,
    ):
        super().__init__(name, profile, **kwargs)
        self._init_actions([GenerateUnitTests, RunTests])

    async def _act(self) -> Message:
        todo = self._rc.todo
        msg = self._rc.memory.get()[-1]

        if isinstance(todo, GenerateUnitTests):
            code = msg.content
            result = await GenerateUnitTests().run(code)

        elif isinstance(todo, RunTests):
            tests = msg.content
            result = await RunTests().run(tests)

        return Message(content=result, role=self.profile, cause_by=todo)
