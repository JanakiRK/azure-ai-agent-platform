from src.agent import Agent

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