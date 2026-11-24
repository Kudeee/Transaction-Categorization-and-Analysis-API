from app import models
from app.utils.password import verify_password


def test_create_user(client, sample_user_register):
    response = client.post("/user/register", json=sample_user_register)

    assert response.status_code == 201

    data = response.json()

    assert data["email"] == "example@example.com"
    assert "id" in data
    assert "password" not in data


def test_register_duplicate_email(client, sample_user_register):
    first_res = client.post("/user/register", json=sample_user_register)
    second_res = client.post("/user/register", json=sample_user_register)

    assert first_res.status_code == 201
    assert second_res.status_code == 409


def test_password_is_hashed(client, sample_user_register, db_session):
    response = client.post("/user/register", json=sample_user_register)

    assert response.status_code == 201

    user = (
        db_session.query(models.User)
        .filter(models.User.email == "example@example.com")
        .first()
    )

    assert user is not None
    assert user.password != "password123"

    assert verify_password("password123", user.password)
