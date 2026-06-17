import json

import boto3

from botocore.config import Config

from contracts.execution_plugin import ExecutionPlugin

from contracts.execution_result import ExecutionResult


class StepFunctionPlugin(ExecutionPlugin):

    def __init__(self):

        self.client = boto3.client(
            "stepfunctions",
            config=Config(
                retries={"max_attempts": 3, "mode": "standard"}, region_name="sa-east-1"
            ),
        )

    async def execute(self, arn: str, payload: dict) -> ExecutionResult:

        response = self.client.start_execution(
            stateMachineArn=arn,
            input=json.dumps(payload),
        )

        return ExecutionResult(
            execution_id=response["executionArn"],
            status="STARTED",
            metadata=response,
        )
