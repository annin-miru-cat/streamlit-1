import streamlit as st
import os
from google import genai
from dotenv import load_dotenv
#from google.types import GenerateContentConfig
load_dotenv()
client = genai.Client(api_key = os.getenv("API"))
configs = {"system_instruction":"你是一隻貓叫做阿吉",
            "temperature":1}

response = client.models.generate_content( model='gemini-3-flash-preview', config=configs, contents='Suggest some scenarios.')
is_dark_mode = st.checkbox("深色模式")
st.write(response.text)

if is_dark_mode:
    bg_color = "#0E1117"
    text_color = "#FFFFFF"
    st.write(" 晚安！")
else:
    bg_color = "#FFFFFF"
    text_color = "#000000"
    st.write(" 早安！")

st.markdown(f"""
    <style>.stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    </style>
    """, unsafe_allow_html=True)
st.write("Hello, Streamlit!")
st.title("大標題")
st.header("副標題")
st.write("一般文字")
x = 11
y = 6
st.write(x+y)
st.write(x*y)
st.write(x/y)
st.write(x//y)
st.write(x%y)
user_name = st.text_input("請問你的大名？")
if user_name:
    st.write(f" 歡迎來到 Python 課程，{user_name} 同學！")
birth_year = st.number_input(
    "請輸入你的出生西元年",
    1900, 2026, 1995
)
age = 2026 - birth_year
st.write(f"你的年紀 {age}")
