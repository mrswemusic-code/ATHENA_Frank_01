from pprint import pprint

from src.core.kernel.kernel import AthenaKernel
from src.core.brain.brain import AthenaBrain


kernel=AthenaKernel()
kernel.boot()

brain=AthenaBrain(kernel)


print("\n--- STATUS ---")
print(brain.think("estado"))


memory=kernel.get("memory")

memory.remember(

    key="usuario",

    value="Francesco",

    category="profile",

    persistent=True

)

print("\n--- RECALL ---")

pprint(

    memory.recall("usuario")

)

print("\n--- SEARCH ---")

pprint(

    memory.search("francesco")

)

