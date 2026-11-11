import pytest

from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_index(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert "message" in resp.get_json()


def test_health(client):
    assert client.get("/health").get_json() == {"status": "ok"}


def test_calc_add(client):
    assert client.get("/calc/add/2/3").get_json()["result"] == 5


def test_calc_div_by_zero(client):
    assert client.get("/calc/div/1/0").status_code == 400


def test_calc_unknown_op(client):
    assert client.get("/calc/pow/2/3").status_code == 400
