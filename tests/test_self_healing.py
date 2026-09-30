from core.agent import Agent
from core.swarm import Swarm
from core.decision_engine import DecisionEngine
from core.monitoring import MonitoringAgent
from core.self_healing import SelfHealingEngine


def create_engine():
    agent_a = Agent(
        "A",
        workload=0.2,
        reliability=0.95,
        capabilities={
            "restart_service",
            "free_memory",
            "reduce_load",
        },
    )

    agent_b = Agent(
        "B",
        workload=0.4,
        reliability=0.90,
        capabilities={
            "restart_service",
            "free_memory",
            "reduce_load",
        },
    )

    swarm = Swarm([agent_a, agent_b])
    decision_engine = DecisionEngine(swarm)

    return SelfHealingEngine(decision_engine)


def test_healthy_system_requires_no_action():

    monitor = MonitoringAgent()

    metrics = monitor.collect_metrics(
        cpu_usage=0.40,
        memory_usage=0.50,
        response_time=0.5,
        error_rate=0.02,
        service_available=True,
    )

    result = create_engine().analyze(metrics)

    assert result["status"] == "healthy"
    assert result["action"] is None
    assert result["recovery"] is None


def test_service_failure_triggers_restart():

    monitor = MonitoringAgent()

    metrics = monitor.collect_metrics(
        cpu_usage=0.40,
        memory_usage=0.50,
        response_time=0.5,
        error_rate=0.02,
        service_available=False,
    )

    result = create_engine().analyze(metrics)

    assert result["status"] == "recovered"
    assert result["action"] == "restart_service"
    assert result["decision"]["agent"] == "A"
    assert result["recovery"]["success"] is True
    assert result["recovery"]["verified"] is True


def test_high_memory_triggers_memory_recovery():

    monitor = MonitoringAgent()

    metrics = monitor.collect_metrics(
        cpu_usage=0.40,
        memory_usage=0.95,
        response_time=0.5,
        error_rate=0.02,
        service_available=True,
    )

    result = create_engine().analyze(metrics)

    assert result["status"] == "recovered"
    assert result["action"] == "free_memory"
    assert result["recovery"]["verified"] is True


def test_high_cpu_triggers_load_reduction():

    monitor = MonitoringAgent()

    metrics = monitor.collect_metrics(
        cpu_usage=0.95,
        memory_usage=0.50,
        response_time=0.5,
        error_rate=0.02,
        service_available=True,
    )

    result = create_engine().analyze(metrics)

    assert result["status"] == "recovered"
    assert result["action"] == "reduce_load"
    assert result["recovery"]["verified"] is True