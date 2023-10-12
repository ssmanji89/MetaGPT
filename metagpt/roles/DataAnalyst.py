
# Data Analyst Role for MetaGPT Project

from metagpt.actions import Action
from metagpt.roles import Role
from metagpt.schema import Message

class RunDataAnalysis(Action):

    PROMPT_TEMPLATE = "Run data analysis on the following dataset:\n{dataset}"

    async def run(self, dataset: str):
        # Here, you could integrate data analysis libraries like pandas, NumPy, or call an external service
        analysis_result = "Analysis results will be here"
        return analysis_result

class GenerateReport(Action):

    PROMPT_TEMPLATE = "Generate a report based on the following analysis results:\n{results}"

    async def run(self, results: str):
        # Here, you could generate a PDF or a markdown file containing the report
        report = "Generated report content will be here"
        return report

class DataAnalyst(Role):

    def __init__(
        self,
        name: str = "DataAnalyst",
        profile: str = "DataAnalyst",
        **kwargs,
    ):
        super().__init__(name, profile, **kwargs)
        self._init_actions([RunDataAnalysis, GenerateReport])

    async def _act(self) -> Message:
        todo = self._rc.todo
        msg = self._rc.memory.get()[-1]

        if isinstance(todo, RunDataAnalysis):
            dataset = msg.content
            result = await RunDataAnalysis().run(dataset)

        elif isinstance(todo, GenerateReport):
            results = msg.content
            result = await GenerateReport().run(results)

        return Message(content=result, role=self.profile, cause_by=todo)
