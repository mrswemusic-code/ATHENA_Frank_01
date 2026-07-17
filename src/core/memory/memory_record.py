from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4



@dataclass
class MemoryRecord:


    key: str

    value: str

    category: str = "general"

    language: str = "es"

    confidence: float = 1.0

    memory_id: str = field(
        default_factory=lambda: str(uuid4())
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )



    def to_dict(self):

        return {

            "id": self.memory_id,

            "key": self.key,

            "value": self.value,

            "category": self.category,

            "language": self.language,

            "confidence": self.confidence,

            "created_at": self.created_at

        }
