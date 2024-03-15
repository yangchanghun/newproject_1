import streamlit as st
import pandas as pd

def totals_incomes(dataframe):
    st.title('분류별 매출 분석')
    
    # 데이터 형식 변환
    dataframe['가격'] = dataframe['가격'].astype(int)
    
    # 각 분류별 총 매출 계산
    category_total = dataframe.groupby('분류')['가격'].sum() #분류로 groupby하고 가격을 합산함
    
    # 각 분류별 총 매출 시각화
    st.subheader('각 분류별 총 매출')
    st.bar_chart(category_total)

    # 전체 총 매출 계산 및 출력
    total_sales = dataframe['가격'].sum()
    formatted_total_sales = '{:,.0f}'.format(total_sales)  # 천 단위마다 쉼표를 추가하여 포맷팅
    st.subheader(f'전체 총 매출: {formatted_total_sales}')



