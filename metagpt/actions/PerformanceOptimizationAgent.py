
# PerformanceOptimizationAgent for MetaGPT Project

from metagpt.actions import Action
from metagpt.roles import Role
from metagpt.schema import Message

class CodeProfiler(Action):

    PROMPT_TEMPLATE = "Profile the following Python code to identify performance bottlenecks:\n{code}"

    async def run(self, code: str):
        prompt = self.PROMPT_TEMPLATE.format(code=code)
        rsp = await self._aask(prompt)
        return rsp

class Optimizer(Action):

    PROMPT_TEMPLATE = "Suggest and implement optimizations for the following Python code:\n{code}"

    async def run(self, code: str):
        prompt = self.PROMPT_TEMPLATE.format(code=code)
        rsp = await self._aask(prompt)
        return rsp

class PerformanceOptimizationAgent(Role):

    def __init__(
        self,
        name: str = "PerfOpt",
        profile: str = "PerformanceOptimizationAgent",
        **kwargs,
    ):
        super().__init__(name, profile, **kwargs)
        self._init_actions([CodeProfiler, Optimizer])

    async def _act(self) -> Message:
        todo = self._rc.todo
        msg = self._rc.memory.get()[-1]

        if isinstance(todo, CodeProfiler):
            code = msg.content
            result = await CodeProfiler().run(code)

        elif isinstance(todo, Optimizer):
            code = msg.content
            result = await Optimizer().run(code)

        return Message(content=result, role=self.profile, cause_by=todo)
