from src.model import LocalModel

class Agent:
    def __init__(self, name: str, model=None):
        self.name = name
        self.model = model if model is not None else LocalModel()

    def respond(self, message: str) -> str:
        return self.model.generate(message)