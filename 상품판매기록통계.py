import csv
import streamlit as st
import visualize
import pandas as pd
import matplotlib.pyplot as plt
import sized_item
import season_item

# CSV 파일을 딕셔너리 리스트로 변환하는 함수
def csv_to_dict(csv_file_path):
    data = []
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# 메인 함수
def main():
    st.title('상품 판매량 시각화')

    # CSV 파일 업로드
    uploaded_file = st.file_uploader("CSV 파일 업로드", type=['csv'])
    if uploaded_file is not None:
        # 업로드한 CSV 파일을 데이터프레임으로 변환
        df = pd.read_csv(uploaded_file)
        options = ['판매순', '사이즈별 인기순', '계절별 인기순']
        selected_option = st.selectbox("정렬 기준 선택:", options)

        if selected_option == '판매순':
            visualize.visualize_sales(df)
        elif selected_option == '사이즈별 인기순':
            sized_item.sized(df)
        elif selected_option =='계절별 인기순':
            season_item.seasons_items()

if __name__ == "__main__":
    main()


