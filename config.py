import os
import mongomock

class DevConfig:
   
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGODB_DB'),
        'host': os.getenv('MONGODB_HOST'),
        'username': os.getenv('MONGODB_USER'),
        'password':os.getenv('MONGODB_PASSWORD')
    }

class MockConfig:
      
    MONGODB_SETTINGS = {
        'db': 'FlaskMock',
        'host': 'mongodb://localhost/test_db',  
        'mongo_client_class': mongomock.MongoClient  
    }


