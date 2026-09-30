from core.recovery import RecoveryExecutor


def test_restart_service():

    executor = RecoveryExecutor()

    result = executor.execute("restart_service")

    assert result.success is True
    assert result.action == "restart_service"
    assert executor.verify_recovery(result) is True


def test_free_memory():

    executor = RecoveryExecutor()

    result = executor.execute("free_memory")

    assert result.success is True
    assert result.action == "free_memory"


def test_reduce_load():

    executor = RecoveryExecutor()

    result = executor.execute("reduce_load")

    assert result.success is True
    assert result.action == "reduce_load"


def test_unsupported_action():

    executor = RecoveryExecutor()

    result = executor.execute("delete_server")

    assert result.success is False
    assert executor.verify_recovery(result) is False