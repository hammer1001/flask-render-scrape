from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World2!'

app.run("0.0.0.0")