import streamlit as st

st.set_page_config(page_title="Demo App", page_icon="🚀")

st.title("我的第一個 Streamlit App 🚀")
st.write("成功部署後，你會看到這個畫面！")

name = st.text_input("請輸入你的名字")

if name:
    st.success(f"你好，{name}！")
