import pandas as pd
import streamlit as st

# CSV 파일 읽기

def sized(dataframe):

    # # 사이즈별로 가장 많이 팔린 상품 찾기
    popular_products = dataframe.groupby('사이즈')['상품명'].agg(lambda x: x.value_counts().index[0])

    st.write(popular_products)

