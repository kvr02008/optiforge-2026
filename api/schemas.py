from pydantic import BaseModel, Field


class MetricsRequest(BaseModel):
    cpu_usage: float = Field(ge=0, le=1)
    memory_usage: float = Field(ge=0, le=1)
    response_time: float = Field(ge=0)
    error_rate: float = Field(ge=0)
    service_available: bool


class RecoveryResponse(BaseModel):
    status: str
    action: str | None = None
    detection: dict
    decision: dict | None = None
    recovery: dict | None = None