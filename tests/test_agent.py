from src.agent import Agent
import pytest


def test_agent_rejects_empty_name():
    with pytest.raises(ValueError, match="Agent name cannot be empty"):
        Agent("   ")

def test_agent_responds():
    agent = Agent("Azure Agent")

    response = agent.respond("Hello")

    assert response == "Model response to: Hello"

def test_agent_uses_injected_model():
    class FakeModel:
        def generate(self, prompt: str) -> str:
            return f"Fake response to: {prompt}"

    agent = Agent("Azure Agent", model=FakeModel())

    response = agent.respond("Hello")

    assert response == "Fake response to: Hello"

def test_agent_checks_status():
    agent = Agent("Azure Agent")

    result = agent.check_status()

    assert result == "Agent platform is running"

def test_agent_uses_injected_status_tool():
    def fake_status_tool():
        return "Custom tool is working"

    agent = Agent("Azure Agent", status_tool=fake_status_tool)

    result = agent.check_status()

    assert result == "Custom tool is working"