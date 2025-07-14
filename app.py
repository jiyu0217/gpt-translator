import streamlit as st
import openai

# 🔑 GPT API 키를 streamlit에 안전하게 불러오는 코드
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🎬 문화 맥락까지 번역하는 AI 번역기")

text = st.text_area("영어 영화 대사를 입력하세요:")

if st.button("번역 및 설명 요청") and text:
    with st.spinner("GPT가 번역 중입니다..."):
        prompt = f"""
다음 영어 문장을 자연스럽게 한국어로 번역해줘.  
그리고 이 표현이 담고 있는 문화적, 사회적, 관용적 의미가 있다면 짧고 쉽게 설명해줘.  
예: 미국식 유머, 속어, 관용구, 표현 방식 등

문장: "{text}"

출력 형식은 다음과 같게 해줘:
번역:
설명:
        """
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content
        st.success("결과")
        st.markdown(result)
