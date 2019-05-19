from flask import Flask
from flask_restful import Api, Resource

# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config 
app.config.from_object('project.config.DevelopmentConfig')


class UserPing(Resource):

    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }

api.add_resource(UserPing, '/users/ping')