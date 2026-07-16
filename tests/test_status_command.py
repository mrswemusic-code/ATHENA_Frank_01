from src.core.kernel.kernel import AthenaKernel



kernel = AthenaKernel()


kernel.boot()



commands = kernel.get(
    "commands"
)



result = commands.execute(
    "status"
)



print()

print(
    "ATHENA STATUS"
)

print(
    "=============="
)


for key,value in result.items():

    print(
        key,
        ":",
        value
    )
