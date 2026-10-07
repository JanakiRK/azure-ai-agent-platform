class Agent:
    def __init__(self, name: str):
        self.name = name

    def respond(self, message: str) -> str:
        return f"{self.name} received: {message}"