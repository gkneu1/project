import streamlit as st

# 콘텐츠 데이터 (중학생, 고등학생 분리)
content = {
    "middle": {
        "music": [
            ("편안한 피아노 음악 (중학생)", "https://www.youtube.com/watch?v=1ZYbU82GVz4"),
            ("자연 소리와 함께하는 힐링 음악 (중학생)", "https://www.youtube.com/watch?v=1r8hj72bfGo"),
            ("편안한 기타 연주 (중학생)", "https://www.youtube.com/watch?v=2OEL4P1Rz04"),
        ],
        "text": [
            "“중학생 여러분, 지금도 충분히 잘하고 있어요. 천천히, 꾸준히 걸어가면 됩니다.”",
            "“오늘도 최선을 다한 당신, 작은 휴식이 큰 힘이 될 거예요.”",
            "“작은 성공도 스스로 칭찬해 주세요. 당신은 멋진 학생입니다.”",
        ],
        "video": [
            ("자연 풍경 영상 (중학생)", "https://www.youtube.com/watch?v=OdIJ2x3nxzQ"),
            ("동물과 함께하는 힐링 영상 (중학생)", "https://www.youtube.com/watch?v=8ZjpI6fgYSY"),
            ("명상 가이드 영상 (중학생)", "https://www.youtube.com/watch?v=inpok4MKVLM"),
        ],
    },
    "high": {
        "music": [
            ("재즈 피아노 음악 (고등학생)", "https://www.youtube.com/watch?v=5qap5aO4i9A"),
            ("힐링 앰비언트 음악 (고등학생)", "https://www.youtube.com/watch?v=DWcJFNfaw9c"),
            ("클래식 음악 모음 (고등학생)", "https://www.youtube.com/watch?v=GRxofEmo3HA"),
        ],
        "text": [
            "“고등학생 여러분, 힘든 시간도 지나갈 거예요. 당신은 충분히 강합니다.”",
            "“모든 일에는 때가 있으니 너무 조급해하지 말고 자신을 믿으세요.”",
            "“오늘의 작은 성취가 내일의 큰 발전으로 이어질 거예요.”",
        ],
        "video": [
            ("자연과 명상의 조화 영상 (고등학생)", "https://www.youtube.com/watch?v=6p_yaNFSYao"),
            ("ASMR 집중 명상 영상 (고등학생)", "https://www.youtube.com/watch?v=2aNlyJbzGJg"),
            ("심리 상담 팁 영상 (고등학생)", "https://www.youtube.com/watch?v=Yq_6zv2TvG4"),
        ],
    }
}

st.title("📚 청소년 학업 스트레스 해소 앱")

# 이름 입력
name = st.text_input("이름을 입력해주세요")

# 나이 입력
age = st.number_input("나이를 입력하세요 (만)", min_value=10, max_value=19, step=1)

if name and age:
    # 연령대 구분
    if age <= 14:
        group = "middle"
        st.markdown(f"👋 안녕하세요, {name}님! 중학생 여러분 환영합니다!")
    else:
        group = "high"
        st.markdown(f"👋 안녕하세요, {name}님! 고등학생 여러분 환영합니다!")

    method = st.selectbox("스트레스를 어떤 방법으로 풀고 싶나요?", ("음악", "글", "영상"))

    st.markdown("---")

    if method == "음악":
        st.subheader("🎵 추천 음악")
        title, url = content[group]["music"][0]  # 첫 번째 추천 음악
        st.markdown(f"[{title}]({url})")

    elif method == "글":
        st.subheader("📝 위로가 되는 글")
        text = content[group]["text"][0]  # 첫 번째 추천 글
        st.markdown(f"> {text}")

    elif method == "영상":
        st.subheader("🎥 추천 영상")
        title, url = content[group]["video"][0]  # 첫 번째 추천 영상
        st.markdown(f"[{title}]({url})")

    st.markdown("---")
    st.success(f"{name}님, 스트레스가 조금은 풀렸길 바랄게요 😊")

elif not name:
    st.warning("이름을 입력해주세요.")

elif not age:
    st.warning("나이를 입력해주세요.")

st.markdown("🧠 마음이 힘들 때는 선생님이나 상담센터에 꼭 도움을 요청하세요.")
