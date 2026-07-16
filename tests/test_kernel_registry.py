from src.core.kernel.kernel import AthenaKernel


kernel = AthenaKernel()


kernel.boot()


print("\nKERNEL STATUS")

print(
    kernel.status()
)


print("\nCOMPONENT CHECK")


for component in kernel.registry.list():

    result = kernel.get(component)

    print(
        component,
        "OK" if result else "ERROR"
    )


kernel.start()


import time

time.sleep(3)


kernel.stop()
