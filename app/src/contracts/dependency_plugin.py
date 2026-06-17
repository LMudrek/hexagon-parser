from abc import ABC, abstractmethod

from contracts.dependency_result import DependencyResult


class DependencyPlugin(ABC):

    @abstractmethod
    async def execute(self, payload: dict, rule: dict) -> DependencyResult:
        pass
