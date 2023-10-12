
# CodeModularityAgent for MetaGPT Project

from metagpt.actions import Action
from metagpt.roles import Role
from metagpt.schema import Message

class FunctionDecomposer(Action):

    PROMPT_TEMPLATE = "Decompose the following Python function into smaller, more focused functions:\n{code}"

    async def run(self, code: str):
        prompt = self.PROMPT_TEMPLATE.format(code=code)
        rsp = await self._aask(prompt)
        return rsp

class ClassOrganizer(Action):

    PROMPT_TEMPLATE = "Organize the following Python functions into appropriate classes:\n{code}"

    async def run(self, code: str):
        prompt = self.PROMPT_TEMPLATE.format(code=code)
        rsp = await self._aask(prompt)
        return rsp

class CodeModularityAgent(Role):

    def __init__(
        self,
        name: str = "CodeModular",
        profile: str = "CodeModularityAgent",
        **kwargs,
    ):
        super().__init__(name, profile, **kwargs)
        self._init_actions([FunctionDecomposer, ClassOrganizer])

    async def _act(self) -> Message:
        todo = self._rc.todo
        msg = self._rc.memory.get()[-1]

        if isinstance(todo, FunctionDecomposer):
            code = msg.content
            result = await FunctionDecomposer().run(code)

        elif isinstance(todo, ClassOrganizer):
            code = msg.content
            result = await ClassOrganizer().run(code)

        return Message(content=result, role=self.profile, cause_by=todo)
