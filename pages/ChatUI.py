import streamlit as st
from streamlit_chat import message
import requests
from audio_recorder_streamlit import audio_recorder
from streamlit_webrtc import webrtc_streamer
from core import chat_api

chatbot = chat_api.ChatBot()

left_column, right_column = st.columns(2)
with left_column:
    st.image("images/musk.jpeg", caption="This is an example: Elon Musk")

class ChatUI():
    def __init__(self, chatbot=chatbot):
        self.chatbot = chatbot
        self.user_input = None
        if 'generated' not in st.session_state:
            st.session_state['generated'] = []
        if 'past' not in st.session_state:
            st.session_state['past'] = []
    def get_text(self, key):
        self.user_input = st.text_input("Start Chat with your digital life!",key=key)
    def get_audio(self):
        audio_bytes = audio_recorder()
        if audio_recorder: st.audio(audio_bytes, format='audio/wav')
        # webrtc_streamer(key='demo')
    def get_respose(self):
        
        output = self.chatbot.question(self.user_input)
        st.session_state.past.append(self.user_input)
        st.session_state.generated.append(output)
    def display(self, key="display"):
        self.get_text(key=key)
        self.get_audio()
        if self.user_input:
            self.get_respose()
        st.divider()

        if st.session_state['generated']:
            for i in range(len(st.session_state['generated'])-1, -1, -1):
                message(st.session_state["generated"][i], key=str(i))
                message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        
chatui = ChatUI()
with right_column:
    chatui.display(key="qwe")
