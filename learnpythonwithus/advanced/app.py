from flask import Flask

app = Flask(__name__)

@app.route("/greet")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run('localhost', port=5004, debug=True)
