import streamlit as st
import pandas as pd

st.title("📊 데이터 보기")
df = pd.read_csv("heart_failure.csv")
st.dataframe(df)
st.metric("환자 수", f"{len(df)}명")
