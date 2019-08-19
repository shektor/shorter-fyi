import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app().test_client()

    yield app


def test_basic_setup(client):
    return_value = client.get('/')

    assert b'ShorterFYI - A URL shortener' in return_value.data
