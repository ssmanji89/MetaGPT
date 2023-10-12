
# CommunityEngagementAgent for MetaGPT Project

from metagpt.actions import Action
from metagpt.roles import Role
from metagpt.schema import Message

class GenerateContributingGuide(Action):

    PROMPT_TEMPLATE = "Generate a CONTRIBUTING.md guide based on the following project details:\n{name}\n{description}\n{requirements}"

    async def run(self, name: str, description: str, requirements: str):
        prompt = self.PROMPT_TEMPLATE.format(name=name, description=description, requirements=requirements)
        rsp = await self._aask(prompt)
        return rsp

class IssueResponder(Action):

    PROMPT_TEMPLATE = "Generate an initial response for the following GitHub issue:\n{issue}"

    async def run(self, issue: str):
        prompt = self.PROMPT_TEMPLATE.format(issue=issue)
        rsp = await self._aask(prompt)
        return rsp

class CommunityEngagementAgent(Role):

    def __init__(
        self,
        name: str = "CommunityMgr",
        profile: str = "CommunityEngagementAgent",
        **kwargs,
    ):
        super().__init__(name, profile, **kwargs)
        self._init_actions([GenerateContributingGuide, IssueResponder])

    async def _act(self) -> Message:
        todo = self._rc.todo
        msg = self._rc.memory.get()[-1]

        if isinstance(todo, GenerateContributingGuide):
            details = msg.content
            name, description, requirements = details.split("\n")
            result = await GenerateContributingGuide().run(name, description, requirements)

        elif isinstance(todo, IssueResponder):
            issue = msg.content
            result = await IssueResponder().run(issue)

        return Message(content=result, role=self.profile, cause_by=todo)
