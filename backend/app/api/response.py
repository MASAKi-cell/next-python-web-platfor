from os.path import join
import openai
from config import openai_api_key

tmpPath = "/Users/takahashi_masaki/Desktop/Whisper-chatGTP-Api/backend/s.wav"


# 音声をWhisper APIで文字に変換する関数
def voice_to_text() -> str:
    try:
        openai.api_key = openai_api_key  # Api Keyのセット
        dotenv_path = join(tmpPath)
        audio_file = open(dotenv_path, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript["text"]
    except openai.OpenAIError as error:
        print(f"Error in the audio: {error}")
        return "Error in processing the audio"


# chat-gtpによる返答文の生成
def think_response(text_message: str) -> str:
    try:
        openai.api_key = openai_api_key  # Api Keyのセット
        chat_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": text_message},
            ],
        )
        return chat_response["choices"][0]["message"]["content"]
    except openai.OpenAIError as error:
        print(f"Error in chat-gtp: {error}")
        return "Error in processing the chat-gtp"
