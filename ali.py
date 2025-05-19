import dashscope
from dashscope.audio.tts_v2 import VoiceEnrollmentService, SpeechSynthesizer

dashscope.api_key = "sk-3d290f3199b7407f8b4cd0e543ef8e8c"

voices = {
    "castorice": "https://cosy-voice-hyg.oss-cn-beijing.aliyuncs.com/castorice.wav",
    "firefly": "https://cosy-voice-hyg.oss-cn-beijing.aliyuncs.com/firefly.wav",
    "silver_wolf": "https://cosy-voice-hyg.oss-cn-beijing.aliyuncs.com/silver-wolf.wav",
    "sparkle": "https://cosy-voice-hyg.oss-cn-beijing.aliyuncs.com/sparkle.wav",
}

prefix = "starrail"
target_model = "cosyvoice-v2"

service = VoiceEnrollmentService()

# voice_ids = {}
# print("Creating voices...")
# for voice_name, voice_url in voices.items():
#     voice_id = service.create_voice(target_model, prefix, voice_url)
#     print("Voice ID: ", voice_id)
#     print("Voice Name: ", voice_name)
#     print("Request ID: ", service.get_last_request_id())
#     voice_ids[voice_name] = voice_id
# print("Voice IDs: ", voice_ids)

voices = service.list_voices()

print("Waiting for voice enrollment to complete...")
for voice in voices:
    voice_id = voice["voice_id"]
    synthesizer = SpeechSynthesizer(model=target_model, voice=voice_id)
    text = "每次看见可爱的事物，我总想把它们做成小玩偶...羊毛毡可以把造型做得最还原，用绒线钩织和牛奶棉填充的话，摸着会更软一些。不止是小动物，也可以制作扎格列斯的银币娃娃、不同表情的水煮嘟噜蛋娃娃...抱着它们，睡眠总是格外安稳香甜。"
    audio = synthesizer.call(text)
    # print("Voice Name: ", voice_name)
    print("Voice ID: ", voice_id)
    print("Request ID: ", synthesizer.get_last_request_id())

    with open(f"./aliyun/{voice_id}.wav", "wb") as f:
        f.write(audio)
    print(f"Audio saved to ./aliyun/{voice_id}.wav")

print("All voices enrolled and audio files saved.")
