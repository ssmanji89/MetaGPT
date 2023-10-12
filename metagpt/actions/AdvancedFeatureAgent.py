
# AdvancedFeatureAgent for MetaGPT Project

from metagpt.actions.action import Action
from metagpt.roles import Role
from metagpt.schema import Message

class ImplementCollaboration(Action):

    PROMPT_TEMPLATE = "Design a system for real-time collaboration for the following project:\n{name}\n{description}"

    async def run(self, name: str, description: str):
        prompt = self.PROMPT_TEMPLATE.format(name=name, description=description)
        rsp = await self._aask(prompt)
        return rsp

class CreateGUI(Action):

    PROMPT_TEMPLATE = "Design a basic graphical user interface (GUI) for the following project:\n{name}\n{description}"

    async def run(self, name: str, description: str):
        prompt = self.PROMPT_TEMPLATE.format(name=name, description=description)
        rsp = await self._aask(prompt)
        return rsp

class AdvancedFeatureAgent(Role):

    def __init__(
        self,
        name: str = "AdvancedFeature",
        profile: str = "AdvancedFeatureAgent",
        **kwargs,
    ):
        super().__init__(name, profile, **kwargs)
        self._init_actions([ImplementCollaboration, CreateGUI])

    async def _act(self) -> Message:
        todo = self._rc.todo
        msg = self._rc.memory.get()[-1]

        if isinstance(todo, ImplementCollaboration):
            details = msg.content
            name, description = details.split("\n")
            result = await ImplementCollaboration().run(name, description)

        elif isinstance(todo, CreateGUI):
            details = msg.content
            name, description = details.split("\n")
            result = await CreateGUI().run(name, description)

        return Message(content=result, role=self.profile, cause_by=todo)
