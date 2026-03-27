import streamlit as st

st.title("노래 추천 서비스")

_, main, _ = st.columns([1, 10, 1])

with main:
    _, image, _ = st.columns([1, 1, 1])

    with image:
        st.image("static/images/songLogo.png", width=150)
    
    st.markdown(
        """
        ## 당신의 음악 취향을 분석하여 맞춤형 노래를 추천해드립니다!
        - 지금 바로 로그인하여 나만의 플레이리스트를 만들어보세요!
        - 로그인 후, 좋아하는 노래를 선택하면 AI가 당신의 음악 취향을 분석하여 새로운 노래를 추천해드립니다."""
    )