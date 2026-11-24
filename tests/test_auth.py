def test_login(client, sample_user_login, sample_user_register):
    client.post("/user/register", json=sample_user_register)

    response = client.post("/login/", data=sample_user_login)

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_incorrect_password(client, sample_user_login, sample_user_register):
    client.post("/user/register", json=sample_user_register)

    response = client.post(
        "/login/",
        data={"username": sample_user_login["username"], "password": "wrongpassword"},
    )

    assert response.status_code == 401


def test_login_nonexistent_user(client):
    response = client.post(
        "/login/", data={"username": "unknown@example.com", "password": "password123"}
    )

    assert response.status_code == 401


def test_access_protected_route(client, sample_user_login, sample_user_register):
    # Register
    client.post("/user/register", json=sample_user_register)

    # Login
    login_response = client.post("/login/", data=sample_user_login)

    token = login_response.json()["access_token"]

    # Access protected endpoint
    response = client.get("/user/me", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert response.json()["email"] == sample_user_login["username"]
