from core.monitoring import MonitoringAgent
from core.anomaly_detection import AnomalyDetector


def test_normal_system():

    monitor = MonitoringAgent()

    metrics = monitor.collect_metrics(
        cpu_usage=0.40,
        memory_usage=0.50,
        response_time=0.5,
        error_rate=0.02,
        service_available=True,
    )

    detector = AnomalyDetector()

    result = detector.detect(metrics)

    assert result["anomaly_detected"] is False
    assert result["severity"] == "normal"


def test_high_cpu_detection():

    monitor = MonitoringAgent()

    metrics = monitor.collect_metrics(
        cpu_usage=0.95,
        memory_usage=0.50,
        response_time=0.5,
        error_rate=0.02,
        service_available=True,
    )

    result = AnomalyDetector().detect(metrics)

    assert result["anomaly_detected"] is True
    assert "high_cpu" in result["anomalies"]


def test_service_failure():

    monitor = MonitoringAgent()

    metrics = monitor.collect_metrics(
        cpu_usage=0.40,
        memory_usage=0.50,
        response_time=0.5,
        error_rate=0.02,
        service_available=False,
    )

    result = AnomalyDetector().detect(metrics)

    assert result["severity"] == "critical"
    assert "service_failure" in result["anomalies"]


def test_multiple_anomalies():

    monitor = MonitoringAgent()

    metrics = monitor.collect_metrics(
        cpu_usage=0.95,
        memory_usage=0.90,
        response_time=3.0,
        error_rate=0.20,
        service_available=True,
    )

    result = AnomalyDetector().detect(metrics)

    assert result["anomaly_detected"] is True
    assert result["severity"] == "high"


def test_negative_metric_rejected():

    monitor = MonitoringAgent()

    try:
        monitor.collect_metrics(
            cpu_usage=-0.1,
            memory_usage=0.5,
            response_time=0.5,
            error_rate=0.02,
            service_available=True,
        )
        assert False
    except ValueError:
        assert True