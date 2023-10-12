
# Enhanced ErrorHandlingAgent for MetaGPT Project

from metagpt.actions import Action
from metagpt.roles import Role
from metagpt.schema import Message

class AddTryCatch(Action):

    def insert_try_catch(self, code: str) -> str:
        # Here, you can use GPT API to insert try-catch blocks in the given code
        # e.g., rsp = GPT_API.insert_try_catch(code)
        rsp = "Code with try-catch blocks will be here"
        return rsp

    async def run(self, code: str):
        updated_code = self.insert_try_catch(code)
        return updated_code

class GenerateErrorLog(Action):

    def create_error_log(self, code: str) -> str:
        # Here, you can use GPT API to generate an error logging system based on the code
        # e.g., rsp = GPT_API.create_error_log(code)
        rsp = "Generated error logging system will be here"
        return rsp

    async def run(self, code: str):
        error_log = self.create_error_log(code)
        return error_log

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
