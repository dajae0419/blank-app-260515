import streamlit as st

st.title("자기소개")

st.header("이름")
st.write("여기에 이름을 입력하세요.")

st.header("사진")
# st.image("프로필_사진.jpg", caption="프로필 사진")  # 사진 파일 경로를 지정하세요

st.header("소개")
st.write("여기에 간단한 자기소개를 입력하세요.")

st.header("관심사")
st.write("여기에 관심사를 입력하세요.")

st.header("기술 스킬")
st.write("여기에 기술 스킬을 입력하세요.")
