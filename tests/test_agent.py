from src.agent import Agent


def test_agent_responds():
    agent = Agent("Azure Agent")

    response = agent.respond("Hello")

    assert response == "Azure Agent received: Hello"