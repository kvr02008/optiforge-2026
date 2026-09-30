from dataclasses import dataclass, field
from typing import Set


@dataclass
class Agent:
    agent_id: str
    status: str = "available"
    workload: float = 0.0
    cpu_capacity: float = 1.0
    memory_capacity: float = 1.0
    communication_quality: float = 1.0
    reliability: float = 1.0
    capabilities: Set[str] = field(default_factory=set)

    def is_available(self) -> bool:
        return (
            self.status == "available"
            and self.communication_quality > 0.0
        )

    def can_perform(self, action: str) -> bool:
        return action in self.capabilities