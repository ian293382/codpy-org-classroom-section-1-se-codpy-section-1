from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker! This is docker compose run"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
