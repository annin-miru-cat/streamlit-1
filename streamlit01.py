import streamlit as st
import os
import google.generativeai as genai
from google.colab import userdata
# 讀取金鑰:api_keys 是一個變數,不要加引號
api_keys = userdata.get('GEMINI_KEY')
# 初始化時就定義好它是誰
ai_persona = "你是一個說話優雅的英國管家,叫作阿吉。請稱呼使用者為『主人』。"
model = genai.GenerativeModel(
model_name='gemini-1.5-flash',
system_instruction=ai_persona
)
response = model.generate_content("幫我泡杯茶。")

S=st.text_input("response")
if st.button("click"):
            if S:
                        response = client.models.generate_content( model='gemini-3.1-flash-lite-preview', config=configs, contents=S)
                        st.write(response.text)

