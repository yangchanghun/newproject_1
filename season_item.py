import streamlit as st
import pandas as pd
from collections import defaultdict

def seasons_items(df):
    # 계절별 상품 판매량을 저장할 딕셔너리 생성
    seasonal_product_sales = defaultdict(lambda: defaultdict(int))

    seasons = {
        '봄': [3, 4, 5],
        '여름': [6, 7, 8],
        '가을': [9, 10, 11],
        '겨울': [12, 1, 2]
    }
    
    # 인덱스를 사용하지 않고 DataFrame의 각 행에 대해 반복
    for row in df.itertuples(index=False):
        # 판매날짜 열에서 월 정보를 추출
        month = int(row.판매날짜.split('-')[1])
        
        # 각 계절에 해당하는지 확인하고, 상품 판매량을 저장
        for season, month_list in seasons.items():
            if month in month_list:
                product = row.상품명
                seasonal_product_sales[season][product] += 1

    # 결과를 출력
    for season, product_sales in seasonal_product_sales.items():
        st.write(f"{season} 계절에 팔린 상품")
        # 판매량 데이터를 DataFrame으로 변환하여 표로 출력
        df_season = pd.DataFrame(list(product_sales.items()), columns=['상품명', '판매량'])
        # list(product_sales.items()), columns=['상품명', '판매량']를 데이터프레임으로 변환한다
        
        st.table(df_season)



