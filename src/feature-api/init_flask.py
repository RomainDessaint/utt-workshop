from flask import Flask

app = Flask(__name__)

@app.route('/ping/', methods=['GET'])
def welcome():
    return "PONG!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)