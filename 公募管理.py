import streamlit as st

import pandas as pd

import os



st.title("公募・応募管理アプリ")



file_name = "applications.csv"



# データ読み込み

if os.path.exists(file_name):

    df = pd.read_csv(file_name)

else:

    df = pd.DataFrame(

        columns=["名称", "締切", "状況", "メモ"]

    )



# 入力フォーム

st.header("応募先を追加")



name = st.text_input("名称")

deadline = st.date_input("締切")

status = st.selectbox(

    "状況",

    ["未着手", "応募中", "提出済", "面接予定", "結果待ち", "終了"]

)

memo = st.text_area("メモ")



if st.button("追加"):

    new_row = pd.DataFrame(

        [[name, deadline, status, memo]],

        columns=["名称", "締切", "状況", "メモ"]

    )



    df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv(file_name, index=False)



    st.success("追加しました！")



# 一覧表示

st.header("応募一覧")



if len(df) > 0:

    st.dataframe(df)

else:

    st.write("まだ登録されていません")



