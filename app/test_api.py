from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)


def test_read_item():
    url = 'https://my-talking-tom.en.aptoide.com/app'
    response = client.get("/get/url?url={}".format(url))
    resp = response.json()
    assert response.status_code == 200
    assert 'My Talking Tom' == resp.get('name', '')
    assert '4.4 - 4.4.4+' == resp.get('version', '')
    assert '10.5M' == resp.get('downloads', '')


def test_read_item_not_found():
    url = 'https://notfound.en.aptoide.com/app'
    response = client.get("/get/url?url={}".format(url))
    assert response.status_code == 404
    assert response.json() == {}


def test_read_item_bad():
    url = 'https://my-talking-tom.en.aptoide.net/app'
    response = client.get("/get/url?url={}".format(url))
    assert response.status_code == 400
    assert response.json() == {}
