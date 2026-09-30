from .agent import Agent


def calculate_agent_score(agent: Agent, recovery_cost: float = 0.0) -> float:
    """
    Calculate the suitability score of an agent for a recovery task.

    Higher score means the agent is more suitable.
    All input values are expected to be between 0.0 and 1.0.
    """

    capability_score = 1.0 if agent.capabilities else 0.0

    resource_score = (
        agent.cpu_capacity + agent.memory_capacity
    ) / 2

    communication_score = agent.communication_quality
    reliability_score = agent.reliability

    workload_penalty = agent.workload
    recovery_cost_penalty = recovery_cost

    score = (
        0.15 * capability_score
        + 0.15 * resource_score
        + 0.20 * communication_score
        + 0.25 * reliability_score
        - 0.25 * workload_penalty
        - 0.05 * recovery_cost_penalty
    )

    return max(0.0, min(1.0, score))