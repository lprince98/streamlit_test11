# 이 내용을 app.py 로 저장한 뒤  streamlit run app.py

import streamlit as st
import pandas as pd

# 공통 설정 (모든 페이지에 적용됨)
st.set_page_config(page_title="심부전 분석", page_icon="🫀")

# --- 페이지를 함수로 정의 ---
def home():
    st.title("🫀 심부전 환자 분석")
    st.write("👈 사이드바에서 페이지를 선택하세요.")

def data_page():
    st.title("📊 데이터 보기")
    df = pd.read_csv("heart_failure.csv")
    st.dataframe(df)

def chart_page():
    import matplotlib.pyplot as plt
    st.title("📈 나이 분포")
    df = pd.read_csv("heart_failure.csv")
    fig, ax = plt.subplots()
    ax.hist(df["age"], bins=20, color="#5BAFB8")
    st.pyplot(fig)

# --- 페이지 등록 후 실행 ---
pg = st.navigation([
    st.Page(home,       title="홈",     icon="🏠", default=True),
    st.Page(data_page,  title="데이터", icon="📊"),
    st.Page(chart_page, title="차트",   icon="📈"),
])
pg.run()
