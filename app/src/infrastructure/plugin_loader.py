from functools import lru_cache

from importlib.metadata import entry_points

from contracts.execution_plugin import ExecutionPlugin


@lru_cache(maxsize=32)
def resolve_plugin(plugin_type: str) -> ExecutionPlugin:

    plugins = {ep.name: ep.load() for ep in entry_points(group="aws.plugins")}

    cls = plugins.get(plugin_type)

    if cls is None:

        raise RuntimeError(f"Plugin '{plugin_type}' not found")

    return cls()
