from src.core.memory.memory_engine import MemoryEngine



memory = MemoryEngine()



print("\nATHENA MEMORY TEST\n")



memory.remember(
    "creator",
    "Mr.Swe",
    persistent=True
)



memory.remember(
    "project",
    "ATHENA AI OS",
    persistent=True
)



print(
    "Creator:",
    memory.recall("creator")
)



print(
    "Project:",
    memory.recall("project")
)



print(
    "\nSNAPSHOT"
)


print(
    memory.snapshot()
)
