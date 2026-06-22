import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 나이 분포")
df = pd.read_csv("heart_failure.csv")
fig, ax = plt.subplots()
ax.hist(df["age"], bins=20, color="#5BAFB8")
st.pyplot(fig)
