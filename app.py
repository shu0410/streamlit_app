import streamlit as st
import pandas as pd

st.title("年齢別・男女別人口アプリ")

df = pd.read_csv("population.csv")
st.write(df.head())

pref_list = df["都道府県"].unique()
pref = st.selectbox("都道府県を選択", pref_list)