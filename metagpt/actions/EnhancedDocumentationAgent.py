
# Enhanced DocumentationAgent for MetaGPT Project

from metagpt.actions import Action
from metagpt.roles import Role
from metagpt.schema import Message

class GenerateComments(Action):

    def generate_comments_for_code(self, code: str) -> str:
        # Here, you can use GPT API to generate comments for the code
        # e.g., rsp = GPT_API.generate_comments(code)
        rsp = "Generated comments for the code will be here"
        return rsp

    async def run(self, code: str):
        comments = self.generate_comments_for_code(code)
        return comments

class GenerateReadme(Action):

    def generate_readme(self, description: str) -> str:
        # Here, you can use GPT API to generate a README.md content based on the project description
        # e.g., rsp = GPT_API.generate_readme(description)
        rsp = "Generated README content will be here"
        return rsp

    async def run(self, description: str):
        readme_content = self.generate_readme(description)
        return readme_content

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
