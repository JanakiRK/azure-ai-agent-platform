from src.model import LocalModel
from src.tools import get_current_status

class Agent:
    def __init__(self, name: str, model=None, status_tool=None):
        if not name.strip():
            raise ValueError("Agent name cannot be empty")

        self.name = name
        self.model = model if model is not None else LocalModel()
        self.status_tool = (
            status_tool if status_tool is not None else get_current_status
        )

    def respond(self, message: str) -> str:
        return self.model.generate(message)

    def check_status(self) -> str:
        return self.status_tool()