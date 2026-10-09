from src.model import LocalModel

class Agent:
    def __init__(self, name: str, model=None):
        if not name.strip():
            raise ValueError("Agent name cannot be empty")

        self.name = name
        self.model = model if model is not None else LocalModel()

    def respond(self, message: str) -> str:
        return self.model.generate(message)