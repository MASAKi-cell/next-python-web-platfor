from os.path import join
import openai
from config import openai_api_key


# 音声をWhisper APIで文字に変換する関数
def voice_to_text() -> str:
    openai.api_key = openai_api_key  # Api Keyのセット
    dotenv_path = join(
        "/Users/takahashi_masaki/Desktop/Whisper-chatGTP-Api/backend/asano.wav"
    )
    audio_file = open(dotenv_path, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]


voice_to_text()
