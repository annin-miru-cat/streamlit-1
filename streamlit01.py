import streamlit as st
import google.generativeai as genai

# ── 頁面初始化設定 ──────────────────────────────────────────
st.set_page_config(
    page_title="中科 AI 客服 - 闕老師實戰班",
    page_icon="🤖",
    layout="wide"
)

# ── 自訂 CSS 美化介面 ───────────────────────────────────────
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        font-size: 2rem;
        font-weight: bold;
        color: #1a73e8;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🤖 中科 AI 客服</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">闕老師實戰班 | Powered by Gemini</div>', unsafe_allow_html=True)

# ── API 初始化 ──────────────────────────────────────────────
try:
    apikeys = st.secrets["API"]
    genai.configure(api_key=apikeys)
    model = genai.GenerativeModel(model_name="gemini-2.0-flash")
except Exception as e:
    st.error(f"⚠️ API 初始化失敗：{e}")
    st.stop()

# ── Session State 初始化（對話歷史） ────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# ── 側邊欄設定 ─────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ 設定")

    system_prompt = st.text_area(
        "系統提示詞（角色設定）",
        value="你是一位專業、友善的 AI 客服助理，請用繁體中文回答問題。",
        height=120
    )

    temperature = st.slider("回答創意度（Temperature）", 0.0, 1.0, 0.7, 0.1)

    if st.button("🗑️ 清除對話紀錄", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat = model.start_chat(history=[])
        st.rerun()

    st.divider()
    st.markdown(f"📊 目前對話輪數：**{len(st.session_state.messages) // 2}**")

# ── 顯示歷史對話 ────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── 接收使用者輸入 ──────────────────────────────────────────
if user_input := st.chat_input("請輸入你的問題..."):

    # 顯示使用者訊息
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 呼叫 Gemini API 並顯示回應
    with st.chat_message("assistant"):
        with st.spinner("思考中..."):
            try:
                # 將系統提示詞加入首次訊息
                full_prompt = f"{system_prompt}\n\n使用者問題：{user_input}"

                response = st.session_state.chat.send_message(
                    full_prompt if len(st.session_state.messages) == 1 else user_input,
                    generation_config=genai.GenerationConfig(temperature=temperature)
                )

                reply = response.text
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})

            except Exception as e:
                error_msg = f"❌ 發生錯誤：{e}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
