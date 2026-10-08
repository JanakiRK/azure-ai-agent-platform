from src.model import LocalModel


def test_model_generates_response():
    model = LocalModel()

    response = model.generate("Hello")

    assert response == "Model response to: Hello"