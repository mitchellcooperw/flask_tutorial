from flask import Flask

app = Flask(__name__)

@app.route('/howdy')
def howdy():
    return 'Howdy, World!'