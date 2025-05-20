import streamlit as st
import dashscope
from dashscope.audio.tts_v2 import VoiceEnrollmentService, SpeechSynthesizer
import datetime

dashscope.api_key = "sk-3d290f3199b7407f8b4cd0e543ef8e8c"
service = VoiceEnrollmentService()

st.set_page_config(
    page_title="Cosy Voice",
    layout="centered",
)
st.title("Cosy Voice")

if 'audio_data' not in st.session_state:
    st.session_state.audio_data = None
if 'error_message' not in st.session_state:
    st.session_state.error_message = None
    
with st.form("tts-form"):
    text = st.text_area(
        "请输入要转换的文本",
        placeholder="请输入要转换的文本",
        height=300,
    )
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        voices = service.list_voices()
        voice_ids = [voice["voice_id"] for voice in voices]
        voice_type = st.selectbox(
            "选择音色",
            voice_ids,
            placeholder="选择音色",
        )
    with col3:
        submit_button = st.form_submit_button(
            "生成语音", 
            use_container_width=True
        )

if submit_button:
    if not text:
        st.error("请输入要转换的文本")
        st.stop()
    try:
        with st.spinner("正在生成语音..."):
            synthesizer = SpeechSynthesizer(model="cosyvoice-v2", voice=voice_type)
            st.session_state.audio_data = synthesizer.call(text)
            st.session_state.error_message = None
    except Exception as e:
        st.session_state.error_message = str(e)
        st.session_state.audio_data = None
        st.error(f"生成语音失败: {st.session_state.error_message}")
        st.stop()
        
if st.session_state.audio_data:
    st.audio(st.session_state.audio_data, format="audio/wav")
    st.download_button(
        label="下载语音",
        data=st.session_state.audio_data,
        file_name=f"{voice_type}-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.wav",
        mime="audio/wav",
    )

if st.session_state.error_message:
    st.error(f"发生错误: {st.session_state.error_message}")
