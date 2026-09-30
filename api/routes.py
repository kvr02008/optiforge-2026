from fastapi import APIRouter

from core.monitoring import MonitoringAgent
from core.self_healing import SelfHealingEngine
from api.schemas import MetricsRequest, RecoveryResponse

router = APIRouter()

monitor = MonitoringAgent()


def create_engine() -> SelfHealingEngine:
    from core.agent import Agent
    from core.swarm import Swarm
    from core.decision_engine import DecisionEngine

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

    return SelfHealingEngine(DecisionEngine(swarm))


@router.get("/health")
def health_check() -> dict:
    return {
        "status": "online",
        "service": "OptiForge",
    }


@router.post("/analyze", response_model=RecoveryResponse)
def analyze_metrics(request: MetricsRequest) -> dict:
    metrics = monitor.collect_metrics(
        cpu_usage=request.cpu_usage,
        memory_usage=request.memory_usage,
        response_time=request.response_time,
        error_rate=request.error_rate,
        service_available=request.service_available,
    )

    engine = create_engine()

    return engine.analyze(metrics)