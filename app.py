from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine


app = Flask(__name__)
api = Api(app)
db = MongoEngine(app)


app.config['MONGODB_SETTINGS'] = {
    'db': 'FlaskProject',
    'host': 'mongodb',
    'port': 27017,
    'username': 'admin',
    'password':'admin'
}


class UserModel(db.Document):
    cpf = db.StringField(required=True, unique = True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.EmailField(required=True)
    birth_date = db.DateTimeField(required= True)


class Users(Resource):
    def get(self):
        return {"message": "User_1"}

class User(Resource):
    
    def post(self):
        return {"message":"teste post"}
    
    def get(self,cpf):
        return{"message":cpf}
  

api.add_resource(Users, '/users')
api.add_resource(User, '/user/<string:cpf>','/user')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")