

import pytest

from src.application.execution_service import ExecutionService

from src.contracts.execution_result import ExecutionResult

@pytest.mark.asyncio

async def test_execute(monkeypatch):

    class FakePlugin:

        async def execute(self, arn, payload):

            return ExecutionResult("1","STARTED",{})

    monkeypatch.setattr(

        "application.execution_service.resolve_plugin",

        lambda _: FakePlugin()

    )

    result=await ExecutionService().execute(

        "glue",

        "arn:aws:glue:region:acc:job/test",

        {}

    )

    assert result.execution_id=="1"

