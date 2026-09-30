from .monitoring import SystemMetrics


class AnomalyDetector:
    """Detect abnormal infrastructure conditions."""

    CPU_THRESHOLD = 0.85
    MEMORY_THRESHOLD = 0.85
    RESPONSE_TIME_THRESHOLD = 2.0
    ERROR_RATE_THRESHOLD = 0.10

    def detect(self, metrics: SystemMetrics) -> dict:
        """Analyze metrics and return detected anomalies."""

        anomalies = []

        if metrics.cpu_usage >= self.CPU_THRESHOLD:
            anomalies.append("high_cpu")

        if metrics.memory_usage >= self.MEMORY_THRESHOLD:
            anomalies.append("high_memory")

        if metrics.response_time >= self.RESPONSE_TIME_THRESHOLD:
            anomalies.append("high_latency")

        if metrics.error_rate >= self.ERROR_RATE_THRESHOLD:
            anomalies.append("high_error_rate")

        if not metrics.service_available:
            anomalies.append("service_failure")

        return {
            "anomaly_detected": bool(anomalies),
            "anomalies": anomalies,
            "severity": self._calculate_severity(anomalies),
        }

    @staticmethod
    def _calculate_severity(anomalies: list[str]) -> str:
        if "service_failure" in anomalies:
            return "critical"

        if len(anomalies) >= 2:
            return "high"

        if len(anomalies) == 1:
            return "medium"

        return "normal"