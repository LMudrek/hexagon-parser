from infrastructure.plugin_loader import resolve_plugin

from infrastructure.validators import validate_arn


class ExecutionService:

    async def execute(self, plugin_type: str, arn: str, payload: dict):

        validate_arn(arn)

        print("Resolvendo plugin")

        plugin = resolve_plugin(plugin_type)

        print(f"Executando {plugin}")

        try:
            return await plugin.execute(arn, payload)
        except Exception as e:
            raise RuntimeError(f"Falha ao executar plugin {plugin_type}: {e}")
