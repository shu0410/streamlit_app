import streamlit as st
import pandas as pd

st.title("年齢別・男女別人口アプリ")

df = pd.read_csv("population.csv")
st.write(df.head())

sex = st.radio(
    "表示する性別を選択",
    ["男性", "女性", "両方"]
)

age_min, age_max = st.slider(
    "年齢範囲を選択",
    min_value=0,
    max_value=100,
    value=(0, 100)
)

filtered = df[
    (df["Age Group (5-year intervals)"] >= age_min) &
    (df["Age Group (5-year intervals)"] <= age_max)
]

if sex == "男性":
    show_df = filtered.set_index("年齢")[["男性人口"]]

elif sex == "女性":
    show_df = filtered.set_index("年齢")[["女性人口"]]

else:
    show_df = filtered.set_index("年齢")[["男性人口", "女性人口"]]