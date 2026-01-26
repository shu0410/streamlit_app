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
    (df["age-start"] >= age_min) &
    (df["age-start"] <= age_max)
]

if sex == "男性":
    show_df = filtered.set_index("Age Group (5-year intervals)")[["Male Population"]]

elif sex == "女性":
    show_df = filtered.set_index("Age Group (5-year intervals)")[["Female Population"]]

else:
    show_df = filtered.set_index("Age Group (5-year intervals)")[["Male Population", "Female Population"]]