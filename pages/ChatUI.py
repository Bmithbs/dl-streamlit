import streamlit as st
from streamlit_chat import message
import requests
from audio_recorder_streamlit import audio_recorder
from streamlit_webrtc import webrtc_streamer


left_column, right_column = st.columns(2)
with left_column:
    st.image("images/musk.jpeg", caption="This is an example: Elon Musk")

with right_column:
    st.text_input("Start Chat with your digital life!")
    audio_bytes = audio_recorder()
    if audio_recorder: st.audio(audio_bytes, format='audio/wav')
    # webrtc_streamer(key='demo')
    st.divider()
    message("Who are you", is_user=True)
    message("I am a digital life")


# st.set_page_config(
#     page_title="Streamlit Chat - Demo",
#     page_icon=":robot:"
# )

# API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
# headers = {"Authorization": st.secrets['api_key']}

# st.header("Streamlit Chat - Demo")
# st.markdown("[Github](https://github.com/ai-yash/st-chat)")

# if 'generated' not in st.session_state:
#     st.session_state['generated'] = []

# if 'past' not in st.session_state:
#     st.session_state['past'] = []

# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()

# def get_text():
#     input_text = st.text_input("You: ","Hello, how are you?", key="input")
#     return input_text 


# user_input = get_text()

# if user_input:
#     output = query({
#         "inputs": {
#             "past_user_inputs": st.session_state.past,
#             "generated_responses": st.session_state.generated,
#             "text": user_input,
#         },"parameters": {"repetition_penalty": 1.33},
#     })

#     st.session_state.past.append(user_input)
#     st.session_state.generated.append(output["generated_text"])

# if st.session_state['generated']:

#     for i in range(len(st.session_state['generated'])-1, -1, -1):
#         message(st.session_state["generated"][i], key=str(i))
#         message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')


