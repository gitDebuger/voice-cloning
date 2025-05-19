import base64
import os
import requests

TRAIN_URL = "https://openspeech.bytedance.com//api/v1/mega_tts/audio/upload"
STATUS_URL = "https://openspeech.bytedance.com/api/v1/mega_tts/status"

def upload(app_id, access_token, audio_path, spk_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer;" + access_token,
        "Resource-Id": "volc.megatts.voiceclone",
    }
    encoded_data, audio_format = encode_audio_file(audio_path)
    audios = [{
        "audio_bytes": encoded_data, 
        "audio_format": audio_format
    }]
    data = {
        "appid": app_id, 
        "speaker_id": spk_id, 
        "audios": audios, 
        "source": 2,
        "language": 0, 
        "model_type": 1
    }
    response = requests.post(TRAIN_URL, json=data, headers=headers)
    print("filename: ", audio_path)
    print("status code: ", response.status_code)
    if response.status_code != 200:
        raise Exception("Train Post Error: " + response.text)
    print("Train Post Success")


def encode_audio_file(file_path):
    with open(file_path, 'rb') as audio_file:
        audio_data = audio_file.read()
        encoded_data = str(base64.b64encode(audio_data), "utf-8")
        audio_format = os.path.splitext(file_path)[1][1:]  # 获取文件扩展名作为音频格式
        return encoded_data, audio_format

def get_status(app_id, access_token, spk_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer;" + access_token,
        "Resource-Id": "volc.megatts.voiceclone",
    }
    body = {
        "appid": app_id, 
        "speaker_id": spk_id
    }
    response = requests.post(STATUS_URL, headers=headers, json=body)
    print(response.json())
