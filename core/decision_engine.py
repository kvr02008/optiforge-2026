from typing import Dict, Optional

from .agent import Agent
from .heuristics import calculate_agent_score
from .swarm import Swarm


class DecisionEngine:
    """Selects the most suitable agent for a recovery task."""

    def __init__(self, swarm: Swarm) -> None:
        self.swarm = swarm

    def select_agent(
        self,
        action: str,
        recovery_cost: float = 0.0
    ) -> Optional[Dict[str, object]]:
        """
        Select the available agent with the highest suitability score.
        """

        candidates = self.swarm.get_capable_agents(action)

        if not candidates:
            return None

        scored_agents = []

        for agent in candidates:
            score = calculate_agent_score(
                agent,
                recovery_cost=recovery_cost
            )

            scored_agents.append((agent, score))

        selected_agent, selected_score = max(
            scored_agents,
            key=lambda item: item[1]
        )

        return {
            "agent": selected_agent.agent_id,
            "action": action,
            "score": round(selected_score, 3)
        }