from dataclasses import dataclass

import psutil


@dataclass
class SystemMetrics:
    cpu_usage: float
    memory_usage: float
    response_time: float
    error_rate: float
    service_available: bool


class MonitoringAgent:
    """Collect and validate infrastructure metrics."""

    def collect_metrics(
        self,
        cpu_usage: float,
        memory_usage: float,
        response_time: float,
        error_rate: float,
        service_available: bool,
    ) -> SystemMetrics:
        """Create a validated snapshot of system metrics."""

        values = [
            cpu_usage,
            memory_usage,
            response_time,
            error_rate,
        ]

        if any(value < 0 for value in values):
            raise ValueError("Metrics cannot be negative.")

        return SystemMetrics(
            cpu_usage=cpu_usage,
            memory_usage=memory_usage,
            response_time=response_time,
            error_rate=error_rate,
            service_available=service_available,
        )

    def collect_system_metrics(self) -> SystemMetrics:
        """Collect metrics from the current machine."""

        import time

        start_time = time.perf_counter()

        cpu_usage = psutil.cpu_percent(interval=0.1) / 100
        memory_usage = psutil.virtual_memory().percent / 100

        response_time = time.perf_counter() - start_time

        return SystemMetrics(
            cpu_usage=cpu_usage,
            memory_usage=memory_usage,
            response_time=response_time,
            error_rate=0.0,
            service_available=True,
        )