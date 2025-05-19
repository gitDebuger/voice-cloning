from train.create import upload, get_status
from dotenv import dotenv_values
from use.call import synthesize_speech

if __name__ == "__main__":
    config = dotenv_values(".env")
    app_id = config["APP_ID"]
    access_token = config["Access_Token"]
    speaker_id = config["Speaker_ID"]
    # audio_path = "./resources/silver-wolf.wav"
    # upload(app_id, access_token, audio_path, speaker_id)
    # get_status(app_id, access_token, speaker_id)

    # cluster_id = config["Cluster_ID"]
    # text = "诶呀，最近总是见到你嘛……我在哪儿看见的？这能让你知道吗，嘻嘻～"
    # encoding = "wav"
    # file_path = "./target/sparkle.wav"
    # synthesize_speech(app_id, access_token, speaker_id, cluster_id, text, encoding, file_path)
