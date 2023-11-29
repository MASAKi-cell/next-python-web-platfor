import logging
from flask import Flask, request
from flask_cors import CORS
from utils.exceptions import HttpCode
from local_config import local_pass
from api.response import voice_to_text
from api.voicevox import text_to_voice

app = Flask(__name__)
CORS(app, resources={r"frontend/app/*": {"origins": local_pass}})  # オリジンの設定
logging.getLogger("flask_cors").level = logging.DEBUG  # ログの有効化


@app.route("/upload-audio", methods=["POST"])
def upload_audio():
    # 音声合成処理
    audio_file = request.files["audio"]
    if audio_file:
        chatGtpRes = voice_to_text(audio_file)
        text_to_voice(chatGtpRes)
        return {"success": "text to voice"}, HttpCode.OK
    else:
        return {"error": "No audio file provided"}, HttpCode.BAD_REQUEST


if __name__ == "__main__":
    app.run(port=5001, debug=True)
