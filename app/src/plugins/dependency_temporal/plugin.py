from contracts.dependency_plugin import DependencyPlugin

from contracts.dependency_result import DependencyResult


class DependencyTemporalPlugin(DependencyPlugin):

    def __init__(self):
        pass

    async def execute(self, payload: dict, rule: dict) -> DependencyResult:
        return DependencyResult(result=True, status="", metadata={})
