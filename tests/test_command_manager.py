from src.core.kernel.kernel import AthenaKernel



kernel = AthenaKernel()

kernel.boot()



commands = kernel.get(
    "commands"
)



print()

print(
    "AVAILABLE COMMANDS"
)

print(
    commands.list_commands()
)



print()

print(
    "HELP"
)

print(
    commands.help()
)



print()

print(
    "EXECUTE STATUS"
)


status = commands.execute(
    "status"
)


print(
    status
)
