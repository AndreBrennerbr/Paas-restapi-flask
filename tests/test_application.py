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

    def test_get_user(self,client,valid_user,invalid_user):
        response = client.get('/user/%s' % valid_user["cpf"])
        assert response.status_code == 200
        assert response.json[0]["first_name"] == "André"
        assert response.json[0]["last_name"] == "Brenner"
        assert response.json[0]["cpf"] == "528.770.120-93"
        assert response.json[0]["email"] == "brennerandre99@gamil.com"
        assert response.json[0]["birth_date"]['$date'] == '1999-08-01T00:00:00Z'

        response = client.get('/user/%s' % invalid_user["cpf"])
        assert response.status_code == 400
        assert b'cadastrado' in response.data








