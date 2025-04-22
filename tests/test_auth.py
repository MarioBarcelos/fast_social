import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from pamps.routes.auth import router
from pamps.auth import User, Token

# filepath: pamps/routes/test_auth.py

client = TestClient(router)

@pytest.fixture
def mock_user():
    return User(username="testuser", hashed_password="hashedpassword")

@pytest.fixture
def mock_access_token():
    return "mock_access_token"

@pytest.fixture
def mock_refresh_token():
    return "mock_refresh_token"

@patch("pamps.routes.auth.authenticate_user", new_callable=AsyncMock)
@patch("pamps.routes.auth.create_access_token", new_callable=AsyncMock)
@patch("pamps.routes.auth.create_refresh_token", new_callable=AsyncMock)
def test_login_for_access_token_sucesso(
    mock_create_refresh_token,
    mock_create_access_token,
    mock_authenticate_user,
    mock_user,
    mock_access_token,
    mock_refresh_token,
):
    mock_authenticate_user.return_value = mock_user
    mock_create_access_token.return_value = mock_access_token
    mock_create_refresh_token.return_value = mock_refresh_token

    response = client.post(
        "/token",
        data={"username": "testuser", "password": "password"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    assert response.status_code == 200
    result = response.json()
    assert result["access_token"] == mock_access_token
    assert result["refresh_token"] == mock_refresh_token
    assert result["token_type"] == "bearer"

@patch("pamps.routes.auth.authenticate_user", new_callable=AsyncMock)
def test_login_for_access_token_falha(mock_authenticate_user):
    mock_authenticate_user.return_value = None

    response = client.post(
        "/token",
        data={"username": "wronguser", "password": "wrongpassword"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"

@patch("pamps.routes.auth.validade_token", new_callable=AsyncMock)
@patch("pamps.routes.auth.create_access_token", new_callable=AsyncMock)
@patch("pamps.routes.auth.create_refresh_token", new_callable=AsyncMock)
def test_refresh_token_sucesso(
    mock_create_refresh_token,
    mock_create_access_token,
    mock_validade_token,
    mock_user,
    mock_access_token,
    mock_refresh_token,
):
    mock_validade_token.return_value = mock_user
    mock_create_access_token.return_value = mock_access_token
    mock_create_refresh_token.return_value = mock_refresh_token

    response = client.post(
        "/refresh-token",
        json={"refresh_token": "valid_refresh_token"},
    )

    assert response.status_code == 200
    result = response.json()
    assert result["access_token"] == mock_access_token
    assert result["refresh_token"] == mock_refresh_token
    assert result["token_type"] == "bearer"

@patch("pamps.routes.auth.validade_token", new_callable=AsyncMock)
def test_refresh_token_falha(mock_validade_token):
    mock_validade_token.side_effect = Exception("Invalid token")

    response = client.post(
        "/refresh-token",
        json={"refresh_token": "invalid_refresh_token"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid token"
import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from pamps.routes.auth import router
from pamps.auth import User, Token

# filepath: pamps/routes/test_auth.py

client = TestClient(router)

@pytest.fixture
def mock_user():
    return User(username="testuser", hashed_password="hashedpassword")

@pytest.fixture
def mock_access_token():
    return "mock_access_token"

@pytest.fixture
def mock_refresh_token():
    return "mock_refresh_token"

@patch("pamps.routes.auth.authenticate_user", new_callable=AsyncMock)
@patch("pamps.routes.auth.create_access_token", new_callable=AsyncMock)
@patch("pamps.routes.auth.create_refresh_token", new_callable=AsyncMock)
def test_login_for_access_token_success(
    mock_create_refresh_token,
    mock_create_access_token,
    mock_authenticate_user,
    mock_user,
    mock_access_token,
    mock_refresh_token,
):
    mock_authenticate_user.return_value = mock_user
    mock_create_access_token.return_value = mock_access_token
    mock_create_refresh_token.return_value = mock_refresh_token

    response = client.post(
        "/token",
        data={"username": "testuser", "password": "password"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    assert response.status_code == 200
    result = response.json()
    assert result["access_token"] == mock_access_token
    assert result["refresh_token"] == mock_refresh_token
    assert result["token_type"] == "bearer"

@patch("pamps.routes.auth.authenticate_user", new_callable=AsyncMock)
def test_login_for_access_token_failure(mock_authenticate_user):
    mock_authenticate_user.return_value = None

    response = client.post(
        "/token",
        data={"username": "wronguser", "password": "wrongpassword"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"

@patch("pamps.routes.auth.validade_token", new_callable=AsyncMock)
@patch("pamps.routes.auth.create_access_token", new_callable=AsyncMock)
@patch("pamps.routes.auth.create_refresh_token", new_callable=AsyncMock)
def test_refresh_token_success(
    mock_create_refresh_token,
    mock_create_access_token,
    mock_validade_token,
    mock_user,
    mock_access_token,
    mock_refresh_token,
):
    mock_validade_token.return_value = mock_user
    mock_create_access_token.return_value = mock_access_token
    mock_create_refresh_token.return_value = mock_refresh_token

    response = client.post(
        "/refresh-token",
        json={"refresh_token": "valid_refresh_token"},
    )

    assert response.status_code == 200
    result = response.json()
    assert result["access_token"] == mock_access_token
    assert result["refresh_token"] == mock_refresh_token
    assert result["token_type"] == "bearer"

@patch("pamps.routes.auth.validade_token", new_callable=AsyncMock)
def test_refresh_token_failure(mock_validade_token):
    mock_validade_token.side_effect = Exception("Invalid token")

    response = client.post(
        "/refresh-token",
        json={"refresh_token": "invalid_refresh_token"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid token"

import pytest
from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient
from pamps.routes.auth import router
from pamps.auth import Token, RefreshToken

# filepath: pamps/routes/test_auth.py

client = TestClient(router)

@pytest.fixture
def mock_settings():
    return {
        "ACCESS_TOKEN_EXPIRE_MINUTES": 15,
        "REFRESH_TOKEN_EXPIRE_MINUTES": 60,
    }

@patch("pamps.routes.auth.authenticate_user", return_value={"username": "testuser"})
@patch("pamps.routes.auth.create_access_token", return_value="mock_access_token")
@patch("pamps.routes.auth.create_refresh_token", return_value="mock_refresh_token")
def test_login_for_access_token(
    mock_authenticate_user, mock_create_access_token, mock_create_refresh_token
):
    response = client.post(
        "/token",
        data={"username": "testuser", "password": "testpassword"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == 200
    result = response.json()
    assert result["access_token"] == "mock_access_token"
    assert result["refresh_token"] == "mock_refresh_token"
    assert result["token_type"] == "bearer"

@patch("pamps.routes.auth.validade_token", new_callable=AsyncMock)
@patch("pamps.routes.auth.create_access_token", return_value="mock_access_token")
@patch("pamps.routes.auth.create_refresh_token", return_value="mock_refresh_token")
def test_refresh_token(
    mock_validade_token, mock_create_access_token, mock_create_refresh_token
):
    mock_validade_token.return_value = {"username": "testuser"}
    response = client.post(
        "/refresh-token",
        json={"refresh_token": "mock_refresh_token"},
    )
    assert response.status_code == 200
    result = response.json()
    assert result["access_token"] == "mock_access_token"
    assert result["refresh_token"] == "mock_refresh_token"
    assert result["token_type"] == "bearer"