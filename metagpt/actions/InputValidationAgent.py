
# InputValidationAgent for MetaGPT Project

from metagpt.actions import Action
from metagpt.roles import Role
from metagpt.schema import Message

class ValidateInputs(Action):

    PROMPT_TEMPLATE = "Add validation checks for the inputs of the following Python function:\n{code}"

    async def run(self, code: str):
        prompt = self.PROMPT_TEMPLATE.format(code=code)
        rsp = await self._aask(prompt)
        return rsp

class TypeChecker(Action):

    PROMPT_TEMPLATE = "Add type-checking for the arguments of the following Python function:\n{code}"

    async def run(self, code: str):
        prompt = self.PROMPT_TEMPLATE.format(code=code)
        rsp = await self._aask(prompt)
        return rsp

class InputValidationAgent(Role):

    def __init__(
        self,
        name: str = "InputValidator",
        profile: str = "InputValidationAgent",
        **kwargs,
    ):
        super().__init__(name, profile, **kwargs)
        self._init_actions([ValidateInputs, TypeChecker])

    async def _act(self) -> Message:
        todo = self._rc.todo
        msg = self._rc.memory.get()[-1]

        if isinstance(todo, ValidateInputs):
            code = msg.content
            result = await ValidateInputs().run(code)

        elif isinstance(todo, TypeChecker):
            code = msg.content
            result = await TypeChecker().run(code)

        return Message(content=result, role=self.profile, cause_by=todo)
