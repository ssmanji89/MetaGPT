
# DocumentationAgent for MetaGPT Project

from metagpt.actions import Action
from metagpt.roles import Role
from metagpt.schema import Message

class GenerateComments(Action):

    PROMPT_TEMPLATE = "Generate inline comments for the following Python code:\n{code}"

    async def run(self, code: str):
        prompt = self.PROMPT_TEMPLATE.format(code=code)
        rsp = await self._aask(prompt)
        return rsp

class GenerateReadme(Action):

    PROMPT_TEMPLATE = "Generate a README.md file for the following project description:\n{description}"

    async def run(self, description: str):
        prompt = self.PROMPT_TEMPLATE.format(description=description)
        rsp = await self._aask(prompt)
        return rsp

class DocumentationAgent(Role):

    def __init__(
        self,
        name: str = "DocAgent",
        profile: str = "DocumentationAgent",
        **kwargs,
    ):
        super().__init__(name, profile, **kwargs)
        self._init_actions([GenerateComments, GenerateReadme])

    async def _act(self) -> Message:
        todo = self._rc.todo
        msg = self._rc.memory.get()[-1]

        if isinstance(todo, GenerateComments):
            code = msg.content
            result = await GenerateComments().run(code)

        elif isinstance(todo, GenerateReadme):
            description = msg.content
            result = await GenerateReadme().run(description)

        return Message(content=result, role=self.profile, cause_by=todo)

if __name__ == "__main__":
    # This is a placeholder main block for testing
    pass
