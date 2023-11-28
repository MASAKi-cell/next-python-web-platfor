import json
import requests
from config import voicevox_path
from utils.exceptions import ExceptionsError, HttpCode

speaker = "speaker"
one = 1


# 音声合成処理
def post_audio(text: str) -> bytes | None:
    try:
        param: dict = {"text": text, "speaker": one}
        res = requests.post(f"{voicevox_path}/audio_query", params=param)
        res.raise_for_status()  # HTTPステータスコードのチェック

        return res.json()

    except requests.exceptions.HTTPError as http_err:
        raise ExceptionsError(
            status_code=http_err.response.status_code, message=str(http_err)
        )
    except requests.exceptions.ConnectionError as conn_err:
        raise ExceptionsError(
            status_code=HttpCode.INTERNAL_SERVER_ERROR, message=str(conn_err)
        )
    except Exception as e:
        print(f"An error occurred: {e}")  # その他のエラー
    return None


# 音声をバイトデータに変換
def post_synthesis(audio_query_res: str) -> bytes | None:
    try:
        params = {speaker: one}
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
        raise ExceptionsError(
            status_code=http_err.response.status_code, message=str(http_err)
        )
    except requests.exceptions.ConnectionError as conn_err:
        raise ExceptionsError(
            status_code=HttpCode.INTERNAL_SERVER_ERROR, message=str(conn_err)
        )
    except Exception as e:
        print(f"An error occurred: {e}")  # その他のエラー
    return None


def text_to_voice(text: str):
    res = post_audio(text)
    if res is not None:
        synthesis = post_synthesis(res)
        print(synthesis)


text_to_voice("こんにちは")
