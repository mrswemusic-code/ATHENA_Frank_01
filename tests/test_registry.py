from src.core.registry.registry import AthenaRegistry


registry = AthenaRegistry()

registry.register(
    "runtime",
    object()
)

registry.register(
    "memory",
    object()
)

registry.register(
    "hud",
    object()
)

print()

print("REGISTERED:")

for item in registry.list():

    print(item)

print()

print("TOTAL:")

print(registry.count())
