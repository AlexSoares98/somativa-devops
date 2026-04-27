from src.main import *
from unittest.mock import patch
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    result = root()
    assert result == {"message": "Hello World"}

def test_funcaoteste():
    with patch('random.randint', return_value=12000):
        result = funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12000}


def test_status():
    response = client.get("/status")
    assert response.json() == {"status": "Online"}


def test_perfil():
    response = client.get("/perfil")
    assert response.json() == {
        "nick": "AlexS",
        "plataforma": "Steam",
        "jogo": "Counter-Strike 2",
        "horas_de_jogo": 2850,
        "online": True
    }


def test_inventario():
    with patch("random.choice", return_value="AWP | Asiimov"):
        response = client.get("/inventario")
    assert response.json() == {
        "item_destaque": "AWP | Asiimov",
        "quantidade_itens": 5
    }


def test_mapa():
    with patch("random.choice", return_value="Mirage"):
        response = client.get("/mapa")
    assert response.json() == {
        "mapa_aleatorio": "Mirage"
    }


def test_rank():
    with patch("random.choice", return_value="Supremo"):
        response = client.get("/rank")
    assert response.json() == {
        "rank_atual": "Supremo"
    }
