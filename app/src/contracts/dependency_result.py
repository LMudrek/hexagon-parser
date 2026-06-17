from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class DependencyResult:

    result: bool

    status: str

    metadata: dict
