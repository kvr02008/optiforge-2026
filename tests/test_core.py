from core.agent import Agent
from core.simulation import Simulation
from core.swarm import Swarm


def create_agents():
    agent_a = Agent(
        "A",
        workload=0.2,
        cpu_capacity=0.9,
        memory_capacity=0.8,
        reliability=0.95,
        capabilities={"restart_service"},
    )

    agent_b = Agent(
        "B",
        workload=0.6,
        cpu_capacity=0.7,
        memory_capacity=0.7,
        reliability=0.85,
        capabilities={"restart_service"},
    )

    return agent_a, agent_b


def test_available_agents():
    agent_a, agent_b = create_agents()

    swarm = Swarm([agent_a, agent_b])

    available = swarm.get_available_agents()

    assert len(available) == 2


def test_failed_agent_is_not_selected():
    agent_a, agent_b = create_agents()

    simulation = Simulation([agent_a, agent_b])

    simulation.apply_agent_failure("A")

    decision = simulation.make_decision("restart_service")

    assert decision["agent"] == "B"


def test_communication_failure_changes_decision():
    agent_a, agent_b = create_agents()

    simulation = Simulation([agent_a, agent_b])

    simulation.apply_communication_drop("A")

    decision = simulation.make_decision("restart_service")

    assert decision["agent"] == "B"


def test_workload_spike_changes_decision():
    agent_a, agent_b = create_agents()

    simulation = Simulation([agent_a, agent_b])

    simulation.apply_workload_change("A", 0.95)

    decision = simulation.make_decision("restart_service")

    assert decision["agent"] == "B"


def test_no_capable_agent_returns_none():
    agent_a = Agent(
        "A",
        capabilities={"monitor"},
    )

    simulation = Simulation([agent_a])

    decision = simulation.make_decision("restart_service")

    assert decision is None