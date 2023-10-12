
# LanguageSupportAgent for MetaGPT Project

from metagpt.actions import Action
from metagpt.roles import Role
from metagpt.schema import Message

class TranslateDocs(Action):

    PROMPT_TEMPLATE = "Translate the following documentation text into {language} language:\n{text}"

    async def run(self, text: str, language: str):
        prompt = self.PROMPT_TEMPLATE.format(text=text, language=language)
        rsp = await self._aask(prompt)
        return rsp

class LanguageSupportAgent(Role):

    def __init__(
        self,
        name: str = "LangSupport",
        profile: str = "LanguageSupportAgent",
        **kwargs,
    ):
        super().__init__(name, profile, **kwargs)
        self._init_actions([TranslateDocs])

    async def _act(self) -> Message:
        todo = self._rc.todo
        msg = self._rc.memory.get()[-1]

        if isinstance(todo, TranslateDocs):
            details = msg.content
            text, language = details.split("\n")
            result = await TranslateDocs().run(text, language)

        return Message(content=result, role=self.profile, cause_by=todo)
