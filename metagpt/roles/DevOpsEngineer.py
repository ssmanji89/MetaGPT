
# DevOps Engineer Role for MetaGPT Project

from metagpt.actions import Action
from metagpt.roles import Role
from metagpt.schema import Message

class SetupCICD(Action):

    PROMPT_TEMPLATE = "Set up CI/CD pipeline for the following project requirements:\n{requirements}"

    async def run(self, requirements: str):
        # Here, you could integrate CI/CD tools like Jenkins, GitHub Actions, etc.
        setup_details = "CI/CD setup details will be here"
        return setup_details

class MonitorHealth(Action):

    PROMPT_TEMPLATE = "Monitor the health of the following services:\n{services}"

    async def run(self, services: str):
        # Here, you could integrate monitoring tools like Grafana, Prometheus, etc.
        monitoring_results = "Monitoring results will be here"
        return monitoring_results

class DevOpsEngineer(Role):

    def __init__(
        self,
        name: str = "DevOpsEngineer",
        profile: str = "DevOpsEngineer",
        **kwargs,
    ):
        super().__init__(name, profile, **kwargs)
        self._init_actions([SetupCICD, MonitorHealth])

    async def _act(self) -> Message:
        todo = self._rc.todo
        msg = self._rc.memory.get()[-1]

        if isinstance(todo, SetupCICD):
            requirements = msg.content
            result = await SetupCICD().run(requirements)

        elif isinstance(todo, MonitorHealth):
            services = msg.content
            result = await MonitorHealth().run(services)

        return Message(content=result, role=self.profile, cause_by=todo)
