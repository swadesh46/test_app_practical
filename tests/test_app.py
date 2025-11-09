from app import create_app
import pytest

@pytest.fixture
def client():
    app=create_app()
    app.config['Testing']=True
    with app.test_client() as f:
        yield f

def test(client):
    response=client.get('/')
    response1=client.get('/hello')
    assert response.status_code==200
    assert response1.status_code==200