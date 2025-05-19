import base64
import json
import uuid
import requests

URL = "https://openspeech.bytedance.com/api/v1/tts"

def synthesize_speech(app_id, access_token, speaker_id, cluster_id, text, encoding, file_path):
    headers = {
        "Authorization": f"Bearer;{access_token}"
    }
    data = {
        "app": {
            "appid": app_id,
            "token": "access_token",
            "cluster": cluster_id
        },
        "user": {
            "uid": "388808087185088"
        },
        "audio": {
            "voice_type": speaker_id,
            "encoding": encoding,
            "speed_ratio": 1.3,
            "volume_ratio": 1.0,
            "pitch_ratio": 1.0,
        },
        "request": {
            "reqid": str(uuid.uuid4()),
            "text": text,
            "text_type": "plain",
            "operation": "query",
            "with_frontend": 1,
            "frontend_type": "unitTson"
        }
    }
    try:
        resp = requests.post(URL, json.dumps(data), headers=headers)
        print(resp.status_code)
        if "data" in resp.json():
            data = resp.json()["data"]
            file_to_save = open(file_path, "wb")
            file_to_save.write(base64.b64decode(data))
    except Exception as e:
        e.with_traceback()
