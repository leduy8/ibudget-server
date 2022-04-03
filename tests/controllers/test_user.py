from tests.data_mocker import create_dummy_email, create_dummy_user


class TestRegisterUser:
    def test_success_register_user(self, client):
        response = client.post(
            "/users",
            json={"email": "duy1234@gmail.com", "password": "123456"},
            content_type="application/json",
        )

        assert response.status_code == 200
        assert type(response.data) == bytes
        assert len(response.data.decode("utf-8").split(".")) == 3

    def test_fail_register_user_with_wrong_email_format(self, client):
        response = client.post(
            "/users",
            json={"email": "duy123gmail.com", "password": "123456"},
            content_type="application/json",
        )

        assert response.status_code == 400

    def test_fail_register_user_with_missing_email(self, client):
        response = client.post(
            "/users", json={"password": "123456"}, content_type="application/json"
        )

        assert response.status_code == 400

    def test_fail_register_user_with_missing_passsword(self, client):
        response = client.post(
            "/users",
            json={"email": "duy123@gmail.com"},
            content_type="application/json",
        )

        assert response.status_code == 400

    def test_fail_register_user_with_invalid_email_length(self, client):
        response = client.post(
            "/users",
            json={"email": create_dummy_email(), "password": "123456"},
            content_type="application/json",
        )

        assert response.status_code == 400

    def test_fail_register_user_with_invalid_passsword_length(self, client):
        response = client.post(
            "/users",
            json={"email": "duy123@gmail.com", "password": "12345"},
            content_type="application/json",
        )

        assert response.status_code == 400

    def test_fail_register_user_that_has_already_exists(self, client):
        create_dummy_user()

        response = client.post(
            "/users",
            json={"email": "duy123@gmail.com", "password": "123456"},
            content_type="application/json",
        )

        assert response.status_code == 400
