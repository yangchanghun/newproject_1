import streamlit as st
import pandas as pd

def totals_incomes(dataframe):
    st.title('분류별 매출 분석')
    
    # 데이터 형식 변환
    dataframe['가격'] = pd.to_numeric(dataframe['가격'], errors='coerce')  # 누락된 값(NA)이나 무한대(inf)를 NaN으로 변환
    
    # NaN 값 처리
    dataframe['가격'].fillna(0, inplace=True)  # NaN 값을 0으로 대체
    
    # 각 분류별 총 매출 계산
    category_total_b = dataframe.groupby('분류')['가격'].sum() #분류로 groupby하고 가격을 합산함
    category_total_size=dataframe.groupby('사이즈')['가격'].sum()
    category_total_s=dataframe.groupby('성별')['가격'].sum()

    # 각 분류별 총 매출 시각화
    st.subheader('각 분류별 매출')
    st.bar_chart(category_total_b)
    st.subheader('각 사이즈별 매출')
    st.bar_chart(category_total_size)

    st.subheader('각 성별별 매출')
    st.bar_chart(category_total_s)

    # 전체 총 매출 계산 및 출력
    total_sales = dataframe['가격'].sum()
    formatted_total_sales = '{:,.0f}'.format(total_sales)  # 천 단위마다 쉼표를 추가하여 포맷팅
    st.subheader(f'전체 총 매출: {formatted_total_sales}')



