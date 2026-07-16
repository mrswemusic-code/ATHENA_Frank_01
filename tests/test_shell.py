from src.core.kernel.kernel import AthenaKernel

from src.core.shell.athena_shell import AthenaShell



kernel = AthenaKernel()


kernel.boot()



shell = AthenaShell(
    kernel
)


shell.start()
