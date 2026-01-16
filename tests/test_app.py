import pytest
from app import app as hthh_app

@pytest.fixture()
def app():
    app = hthh_app
    app.config.update({
        "TESTING": True,
        })
    
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

def test_home_html_page_is_rendered(client):
    response = client.get("/")
    assert b'<h1 class="govuk-heading-l">Hard to Heat Homes</h1>' in response.data