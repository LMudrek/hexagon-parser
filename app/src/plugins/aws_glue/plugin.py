import boto3

from botocore.config import Config

from contracts.execution_plugin import ExecutionPlugin

from contracts.execution_result import ExecutionResult


class GluePlugin(ExecutionPlugin):

    def __init__(self):

        self.client = boto3.client(
            "glue",
            config=Config(
                retries={"max_attempts": 3, "mode": "standard"}, region_name="sa-east-1"
            ),
        )

    async def execute(self, arn: str, payload: dict) -> ExecutionResult:

        job_name = arn.split("/")[-1]

        response = self.client.start_job_run(
            JobName=job_name,
            Arguments=payload,
        )

        return ExecutionResult(
            execution_id=response["JobRunId"],
            status="STARTED",
            metadata=response,
        )
