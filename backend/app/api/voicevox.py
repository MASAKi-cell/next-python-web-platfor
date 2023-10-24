import requests


#
def audio_query(text: str) -> str:
    param = {"text": text, "speaker": 1}
    res = requests.post("http://localhost:50021/audio_query", params=param)
    return res.json()
