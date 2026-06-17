from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ExecutionResult:

    execution_id: str

    status: str

    metadata: dict
