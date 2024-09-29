import pytest
from application import create_app


class TestApplication():
    
    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        return app.test_client()
    
    @pytest.fixture
    def valid_user(self):
        return {
            "first_name":"André",
            "last_name":"Brenner",
            "cpf":"528.770.120-93",
            "email":"brennerandre99@gamil.com",
            "birth_date":"1999-08-01"
        }

    @pytest.fixture
    def invalid_user(self):
        return {
            "first_name":"André",
            "last_name":"Brenner",
            "cpf":"528.770.120-97",
            "email":"brennerandre99@gamil.com",
            "birth_date":"1999-08-01"
        }
       
    def test_get_users(self,client):
        response = client.get('/users')
        assert response.status_code == 200


    def test_post_user(self,client,valid_user,invalid_user):
        response = client.post('/user',json= valid_user)
        assert response.status_code == 200
        assert b"sucesso" in response.data

        response = client.post('/user',json= invalid_user)
        assert response.status_code == 400
        assert b"invalid" in response.data







