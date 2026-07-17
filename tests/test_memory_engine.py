from src.core.memory.memory_engine import MemoryEngine



memory = MemoryEngine()



print("\nMEMORY TEST")
print("----------------")


memory.remember(

    "browser",

    "Brave",

    category="preference",

    persistent=True

)



print(

    memory.recall(
        "browser"
    )

)


print("\nSEARCH")

print(

    memory.search(
        "Brave"
    )

)
