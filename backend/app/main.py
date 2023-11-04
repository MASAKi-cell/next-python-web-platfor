from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # オリジンの設定


@app.route("/upload-audio", methods=["POST"])
def hello_world():
    return "<p>Hello, World!!</p>"


if __name__ == "__main__":
    app.run(port=5001, debug=True)
