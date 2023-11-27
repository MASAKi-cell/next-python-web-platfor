import json
import requests
from config import voicevox_path

speaker = "speaker"


# 音声合成処理
def post_audio(text: str) -> str | None:
    try:
        param = {"text": text, "speaker": 1}
        res = requests.post(f"{voicevox_path}/audio_query", params=param)
        return res.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # HTTPエラーの場合
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")  # 接続エラーの場合
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")  # タイムアウトエラーの場合
    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred: {req_err}")  # その他のリクエストエラー
    except Exception as e:
        print(f"An error occurred: {e}")  # その他のエラー
    return None


# 音声をバイトデータに変換
def post_synthesis(audio_query_res: str) -> bytes | None:
    try:
        params = {speaker: 1}
        headers = {"content-type": "application/json"}
        audio_query_res_json = json.dumps(audio_query_res)
        res = requests.post(
            f"{voicevox_path}/synthesis",
            data=audio_query_res_json,
            params=params,
            headers=headers,
        )
        res.raise_for_status()  # HTTPステータスコードのチェック

        return res.content
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # HTTPエラーの場合
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")  # 接続エラーの場合
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")  # タイムアウトエラーの場合
    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred: {req_err}")  # その他のリクエストエラー
    except Exception as e:
        print(f"An error occurred: {e}")  # その他のエラー
    return None


def text_to_voice(text: str):
    res = post_audio(text)
    synthesis = post_synthesis(res)
    print(synthesis)


text_to_voice("こんにちは")
