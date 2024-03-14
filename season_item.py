import csv
from collections import defaultdict
import streamlit as st
# 각 계절에 해당하는 달을 리스트로 정의

def seasons_items():
    seasons = {
        '봄': [3, 4, 5],
        '여름': [6, 7, 8],
        '가을': [9, 10, 11],
        '겨울': [12, 1, 2]
    }

    # 각 계절별로 상품 판매량을 저장할 딕셔너리 초기화
    seasonal_product_sales = defaultdict(lambda: defaultdict(int))

    # CSV 파일 읽기
    with open('543.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sale_month = int(row['판매날짜'].split('-')[1])
            for season, months in seasons.items():
                if sale_month in months:
                    seasonal_product_sales[season][row['상품명']] += 1

    # 결과 출력
    for season, product_sales in seasonal_product_sales.items():
        st.write(f"{season} 계절에 가장 잘 팔린 상품:")    
        best_seller = max(product_sales, key=product_sales.get)
        st.write(f"  - {best_seller}: {product_sales[best_seller]}개")