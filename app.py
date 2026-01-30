import streamlit as st
import pandas as pd

st.title("年齢別・男女別人口アプリ")

st.subheader("アプリの概要")
st.write("年齢別・男女別人口構造を可視化する。")

st.subheader("アプリの目的")
st.write("年齢層による人口を把握するため。")

st.subheader("アプリの使い方")
st.write("サイドバーで表示する性別を選択し、年齢範囲を選択する。すると棒グラフと折れ線グラフの両方に表示される。")

df = pd.read_csv("population.csv")
st.write(df.head())
st.caption("※1920年から2015年までのデータです")

with st.sidebar:

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

st.bar_chart(show_df)

st.line_chart(show_df)



st.warning("⚠ Needs review")

st.text("Read Me!!")
st.download_button(
    label="テキストをダウンロード":
    data="閲覧してくださりありがとうございます。":
    file_name="Thank you.txt":
)