from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
class Staff(Resource):
    def get(self):
        return {'data':{'staffnames': 'Nancy Macharia','specialty': 'Clinical Nurse','gender':'female','licence':[{'id':7856,'dateofissue':'2012-11-20','expiry':'2013-11-21'}]}}

api.add_resource(HelloWorld, '/')
api.add_resource(Staff, '/show/staff')

if __name__ == '__main__':
    app.run(debug=True)