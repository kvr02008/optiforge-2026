from .anomaly_detection import AnomalyDetector
from .monitoring import SystemMetrics
from .decision_engine import DecisionEngine
from .recovery import RecoveryExecutor


class SelfHealingEngine:
    """Coordinates detection, decision-making, recovery, and verification."""

    def __init__(self, decision_engine: DecisionEngine):
        self.decision_engine = decision_engine
        self.detector = AnomalyDetector()
        self.recovery = RecoveryExecutor()

    def analyze(self, metrics: SystemMetrics) -> dict:
        """Detect a problem, choose an action, execute and verify recovery."""

        detection = self.detector.detect(metrics)

        if not detection["anomaly_detected"]:
            return {
                "status": "healthy",
                "action": None,
                "detection": detection,
                "recovery": None,
            }

        action = self._select_action(detection["anomalies"])

        decision = self.decision_engine.select_agent(action)

        recovery_result = self.recovery.execute(action)

        verified = self.recovery.verify_recovery(recovery_result)

        return {
            "status": "recovered" if verified else "recovery_failed",
            "action": action,
            "detection": detection,
            "decision": decision,
            "recovery": {
                "success": recovery_result.success,
                "message": recovery_result.message,
                "verified": verified,
            },
        }

    @staticmethod
    def _select_action(anomalies: list[str]) -> str:
        """Map detected problems to recovery actions."""

        if "service_failure" in anomalies:
            return "restart_service"

        if "high_memory" in anomalies:
            return "free_memory"

        if "high_cpu" in anomalies:
            return "reduce_load"

        if "high_latency" in anomalies:
            return "reduce_load"

        if "high_error_rate" in anomalies:
            return "restart_service"

        return "restart_service"