import asyncio

from application.execution_service import ExecutionService


async def run():
    await ExecutionService().execute("step_function", "arn:aws:", {})
    print("rum")


try:
    asyncio.run(run())
except Exception as e:
    print(f"ERROR - {e}")
