from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/test", methods=["GET"])
def test():
    return "test comment"

@app.route("/")
@cross_origin()
def helloworld():
    return "Hello, world!"


if __name__ == '__main__':
    app.run(debug=True)