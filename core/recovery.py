from dataclasses import dataclass


@dataclass
class RecoveryResult:
    action: str
    success: bool
    message: str


class RecoveryExecutor:
    """Safely simulate infrastructure recovery actions."""

    SUPPORTED_ACTIONS = {
        "restart_service",
        "free_memory",
        "reduce_load",
    }

    def execute(self, action: str) -> RecoveryResult:
        if action not in self.SUPPORTED_ACTIONS:
            return RecoveryResult(
                action=action,
                success=False,
                message=f"Unsupported recovery action: {action}",
            )

        messages = {
            "restart_service": "Service restart simulated successfully.",
            "free_memory": "Memory cleanup simulated successfully.",
            "reduce_load": "System load reduction simulated successfully.",
        }

        return RecoveryResult(
            action=action,
            success=True,
            message=messages[action],
        )

    def verify_recovery(self, result: RecoveryResult) -> bool:
        """Verify whether the recovery action succeeded."""

        return result.success