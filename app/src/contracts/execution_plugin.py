from abc import ABC, abstractmethod

from contracts.execution_result import ExecutionResult


class ExecutionPlugin(ABC):

    @abstractmethod
    async def execute(self, arn: str, payload: dict) -> ExecutionResult:
        pass
