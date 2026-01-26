import streamlit as st
import pandas as pd

st.title("年齢別・男女別人口アプリ")

df = pd.read_csv("population.csv")
st.write(df.head())