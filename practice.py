import streamlit as st


st.title("사용자 정보")

with st.container(border=True):

    name = st.text_input("이름", placeholder= "이름을 입력해주세요 (예: 김현빈)")
    birth_date = st.text_input(
    "생년월일", value="", max_chars=6, placeholder="생년월일을 입력 해주세요 (예: 100102)",
)