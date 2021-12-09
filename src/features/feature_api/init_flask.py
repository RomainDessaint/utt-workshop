from flask import Flask

app = Flask(__name__)

@app.route('/ping/', methods=['GET'])
def welcome():
    return "PONG!"