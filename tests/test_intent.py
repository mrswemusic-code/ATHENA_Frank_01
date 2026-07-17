from src.core.brain.brain import AthenaBrain

from src.core.kernel.kernel import AthenaKernel


kernel = AthenaKernel()

kernel.boot()


brain = AthenaBrain(

    kernel

)


examples = [

    "status",

    "estado",

    "cómo está el sistema",

    "system",

    "hola"

]


for text in examples:

    intent = brain.think(

        text

    )

    print(

        text,

        "->",

        intent

    )
