import streamlit as st
import google.generativeai as genai
# 頁面初始化設定
st.set_page_config(
page_title="中科 AI 客服 - 闕老師實戰班",
page_icon=" ",
layout="wide" # "wide" 可利用全螢幕寬度,適合放置儀表板
)

apikeys = st.secrets["API"]

genai.configure(api_key = apikeys)
model = genai.GenerativeModel(
            model_name = 'gemini-31.-flash-lite',
)

if s := st.chat_input("請輸入你的指令"):
            with st.chat_message("assistant"):
                        re = st.session_state.chat.send_message(s)
                        st.markdown(response.text)
