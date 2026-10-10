from src.tools import get_current_status


def test_get_current_status():
    result = get_current_status()

    assert result == "Agent platform is running"