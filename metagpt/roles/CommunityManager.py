
# Community Manager Role for MetaGPT Project

from metagpt.actions import Action
from metagpt.roles import Role
from metagpt.schema import Message

class AnswerQueries(Action):

    PROMPT_TEMPLATE = "Answer the following user queries:\n{queries}"

    async def run(self, queries: str):
        # Here, you could integrate a customer service tool or forum software
        answers = "Answers to user queries will be here"
        return answers

class ManageForums(Action):

    PROMPT_TEMPLATE = "Manage the forums based on the following criteria:\n{criteria}"

    async def run(self, criteria: str):
        # Here, you could integrate forum management tools or software
        management_results = "Forum management results will be here"
        return management_results

class CommunityManager(Role):

    def __init__(
        self,
        name: str = "CommunityManager",
        profile: str = "CommunityManager",
        **kwargs,
    ):
        super().__init__(name, profile, **kwargs)
        self._init_actions([AnswerQueries, ManageForums])

    async def _act(self) -> Message:
        todo = self._rc.todo
        msg = self._rc.memory.get()[-1]

        if isinstance(todo, AnswerQueries):
            queries = msg.content
            result = await AnswerQueries().run(queries)

        elif isinstance(todo, ManageForums):
            criteria = msg.content
            result = await ManageForums().run(criteria)

        return Message(content=result, role=self.profile, cause_by=todo)
