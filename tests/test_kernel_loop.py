from src.core.kernel.kernel import AthenaKernel
import time



kernel = AthenaKernel()


kernel.boot()



loop = kernel.get(
    "loop"
)



def heartbeat():

    print(
        "ATHENA KERNEL HEARTBEAT"
    )



loop.register(
    heartbeat
)



kernel.start()



time.sleep(5)



kernel.stop()
