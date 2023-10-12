
# Security Analyst Role for MetaGPT Project

from metagpt.actions import Action
from metagpt.roles import Role
from metagpt.schema import Message

class RunSecurityScan(Action):

    PROMPT_TEMPLATE = "Run a security scan on the following codebase:\n{codebase}"

    async def run(self, codebase: str):
        # Here, you could integrate a security scanner like OWASP ZAP or Fortify
        scan_results = "Security scan results will be here"
        return scan_results

class GenerateSecurityReport(Action):

    PROMPT_TEMPLATE = "Generate a security report based on the following scan results:\n{results}"

    async def run(self, results: str):
        # Here, you could generate a PDF or a markdown file containing the security report
        report = "Generated security report will be here"
        return report

class SecurityAnalyst(Role):

    def __init__(
        self,
        name: str = "SecurityAnalyst",
        profile: str = "SecurityAnalyst",
        **kwargs,
    ):
        super().__init__(name, profile, **kwargs)
        self._init_actions([RunSecurityScan, GenerateSecurityReport])

    async def _act(self) -> Message:
        todo = self._rc.todo
        msg = self._rc.memory.get()[-1]

        if isinstance(todo, RunSecurityScan):
            codebase = msg.content
            result = await RunSecurityScan().run(codebase)

        elif isinstance(todo, GenerateSecurityReport):
            results = msg.content
            result = await GenerateSecurityReport().run(results)

        return Message(content=result, role=self.profile, cause_by=todo)
