import numpy as np
import pandas as pd
import streamlit as st

st.title("測試numpy/pandas")
a = np.array([89,71,69,77,63,85,92])
# key用於識別和跟蹤組件的屬性
b = st.number_input("輸入成績:", key = "num_b") 

if st.button("輸入完成"): # True表示按鈕被按下
    a = np.append(a, b) # 把b加到a
    st.write(a)