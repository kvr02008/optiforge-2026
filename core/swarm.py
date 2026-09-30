from typing import List

from .agent import Agent


class Swarm:
    """Manages a collection of autonomous agents."""

    def __init__(self, agents: List[Agent]) -> None:
        self.agents = agents

    def get_available_agents(self) -> List[Agent]:
        """Return agents that are currently available."""
        return [agent for agent in self.agents if agent.is_available()]

    def get_capable_agents(self, action: str) -> List[Agent]:
        """Return available agents capable of performing an action."""
        return [
            agent
            for agent in self.get_available_agents()
            if agent.can_perform(action)
        ]

    def add_agent(self, agent: Agent) -> None:
        """Add an agent to the swarm."""
        self.agents.append(agent)

    def remove_agent(self, agent_id: str) -> None:
        """Remove an agent from the swarm."""
        self.agents = [
            agent for agent in self.agents
            if agent.agent_id != agent_id
        ]

    def get_agent(self, agent_id: str) -> Agent | None:
        """Find an agent by ID."""
        for agent in self.agents:
            if agent.agent_id == agent_id:
                return agent

        return None