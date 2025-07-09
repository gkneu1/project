import streamlit as st

# 콘텐츠 예시 데이터
music_links = [
    ("편안한 피아노 음악", "https://www.youtube.com/watch?v=1ZYbU82GVz4"),
    ("자연 소리와 함께하는 힐링 음악", "https://www.youtube.com/watch?v=1r8hj72bfGo"),
]

reading_texts = [
    "“지금 이 순간에도 충분히 잘하고 있어요. 모든 일에는 때가 있고, 천천히 걸어도 괜찮습니다.”",
    "“오늘 힘들었나요? 당신의 하루가 조금은 가벼워졌으면 좋겠어요.”",
]

video_links = [
    ("마음이 편안해지는 자연 풍경 영상", "https://www.youtube.com/watch?v=OdIJ2x3nxzQ"),
    ("ASMR 집중 명상 영상", "https://www.youtube.com/watch?v=2aNlyJbzGJg"),
]

# 앱 제목
st.title("📚 청소년 학업 스트레스 해소 앱")

# 사용자 입력
age = st.number_input("나이를 입력하세요 (만)", min_value=10, max_value=19, step=1)

# 나이 확인
if age:
    st.markdown(f"🎉 안녕하세요, {age}세 학생 여러분!")

    # 해소 방법 선택
    method = st.selectbox("스트레스를 어떤 방법으로 풀고 싶나요?", ("음악", "글", "영상"))

    st.markdown("---")

    # 콘텐츠 제공
    if method == "음악":
        st.subheader("🎵 추천 음악")
        for title, url in music_links:
            st.markdown(f"- [{title}]({url})")

    elif method == "글":
        st.subheader("📝 위로가 되는 글")
        for text in reading_texts:
            st.markdown(f"> {text}")

    elif method == "영상":
        st.subheader("🎥 추천 영상")
        for title, url in video_links:
            st.markdown(f"- [{title}]({url})")

    st.markdown("---")
    st.success("스트레스가 조금은 풀렸길 바랄게요 😊")

# 하단 안내
st.markdown("🧠 마음이 힘들 때는 선생님이나 상담센터에 꼭 도움을 요청하세요.")
