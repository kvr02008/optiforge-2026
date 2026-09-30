from typing import List

from .agent import Agent
from .decision_engine import DecisionEngine
from .swarm import Swarm


class Simulation:
    """Simulates dynamic changes in a multi-agent environment."""

    def __init__(self, agents: List[Agent]) -> None:
        self.swarm = Swarm(agents)
        self.engine = DecisionEngine(self.swarm)

    def apply_agent_failure(self, agent_id: str) -> bool:
        """Mark an agent as failed."""
        agent = self.swarm.get_agent(agent_id)

        if agent is None:
            return False

        agent.status = "failed"
        return True

    def apply_communication_drop(
        self,
        agent_id: str,
        quality: float = 0.0
    ) -> bool:
        """Reduce an agent's communication quality."""
        agent = self.swarm.get_agent(agent_id)

        if agent is None:
            return False

        agent.communication_quality = max(0.0, min(1.0, quality))
        return True

    def apply_workload_change(
        self,
        agent_id: str,
        workload: float
    ) -> bool:
        """Change an agent's workload."""
        agent = self.swarm.get_agent(agent_id)

        if agent is None:
            return False

        agent.workload = max(0.0, min(1.0, workload))
        return True

    def make_decision(
        self,
        action: str,
        recovery_cost: float = 0.0
    ):
        """Ask the decision engine to select an agent."""
        return self.engine.select_agent(
            action,
            recovery_cost=recovery_cost
        )