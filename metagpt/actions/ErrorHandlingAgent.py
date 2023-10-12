
# ErrorHandlingAgent for MetaGPT Project

from metagpt.actions import Action
from metagpt.roles import Role
from metagpt.schema import Message

class AddTryCatch(Action):

    PROMPT_TEMPLATE = "Insert try-catch blocks in the following Python code:\n{code}"

    async def run(self, code: str):
        prompt = self.PROMPT_TEMPLATE.format(code=code)
        rsp = await self._aask(prompt)
        return rsp

class GenerateErrorLog(Action):

    PROMPT_TEMPLATE = "Generate an error logging system for the following Python code:\n{code}"

    async def run(self, code: str):
        prompt = self.PROMPT_TEMPLATE.format(code=code)
        rsp = await self._aask(prompt)
        return rsp

class ErrorHandlingAgent(Role):

    def __init__(
        self,
        name: str = "ErrHandler",
        profile: str = "ErrorHandlingAgent",
        **kwargs,
    ):
        super().__init__(name, profile, **kwargs)
        self._init_actions([AddTryCatch, GenerateErrorLog])

    async def _act(self) -> Message:
        todo = self._rc.todo
        msg = self._rc.memory.get()[-1]

        if isinstance(todo, AddTryCatch):
            code = msg.content
            result = await AddTryCatch().run(code)

        elif isinstance(todo, GenerateErrorLog):
            code = msg.content
            result = await GenerateErrorLog().run(code)

        return Message(content=result, role=self.profile, cause_by=todo)

if __name__ == "__main__":
    # This is a placeholder main block for testing
    pass
