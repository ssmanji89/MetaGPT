
# Quality Assurance (QA) Agent Role for MetaGPT Project

from metagpt.actions import Action
from metagpt.roles import Role
from metagpt.schema import Message

class RunTests(Action):

    PROMPT_TEMPLATE = "Run the following test cases:\n{test_cases}"

    async def run(self, test_cases: str):
        # Here, you could integrate a testing framework like pytest or unittest
        test_results = "Test results will be here"
        return test_results

class GenerateTestReport(Action):

    PROMPT_TEMPLATE = "Generate a test report based on the following test results:\n{results}"

    async def run(self, results: str):
        # Here, you could generate a PDF or a markdown file containing the test report
        report = "Generated test report will be here"
        return report

class QAAgent(Role):

    def __init__(
        self,
        name: str = "QAAgent",
        profile: str = "QAAgent",
        **kwargs,
    ):
        super().__init__(name, profile, **kwargs)
        self._init_actions([RunTests, GenerateTestReport])

    async def _act(self) -> Message:
        todo = self._rc.todo
        msg = self._rc.memory.get()[-1]

        if isinstance(todo, RunTests):
            test_cases = msg.content
            result = await RunTests().run(test_cases)

        elif isinstance(todo, GenerateTestReport):
            results = msg.content
            result = await GenerateTestReport().run(results)

        return Message(content=result, role=self.profile, cause_by=todo)
