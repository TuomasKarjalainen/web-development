from flask import Flask
from flask_restful import Resource,Api
import socket
import cowsay

app = Flask(__name__)
api = Api(app)

class Cowsay(Resource):

    def get(self):
        hostname = socket.gethostname()
        #return {'message': f'This message is from other server: {hostname}'}
        return cowsay.get_output_string('cow', 'this message is from other service') 

api.add_resource(Cowsay, '/')

if __name__ == '__main__':
    app.run(debug=True,port=5051,host="0.0.0.0")