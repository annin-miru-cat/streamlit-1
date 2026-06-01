import streamlit as st
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
