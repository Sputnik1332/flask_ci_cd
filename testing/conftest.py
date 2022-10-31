from _pytest.fixtures import fixture
from flask.testing import FlaskClient
from main import app


@fixture
def client() -> FlaskClient:
    app.config.update(SERVER_NAME='myserver.org')
    with app.test_client() as client:
        with app.app_context():
            yield client
