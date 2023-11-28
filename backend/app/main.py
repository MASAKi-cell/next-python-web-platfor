import logging
from flask import Flask, request
from flask_cors import CORS
from response import voice_to_text
from config import local_pass

app = Flask(__name__)
CORS(app, resources={r"frontend/app/*": {"origins": local_pass}})  # オリジンの設定
logging.getLogger("flask_cors").level = logging.DEBUG  # ログの有効化


@app.route("/upload-audio", methods=["POST"])
def upload_audio():
    audio_file = request.files["audio"]
    chatGtpRes = voice_to_text(audio_file)
    print(chatGtpRes)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
