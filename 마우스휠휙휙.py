import streamlit as st
import pandas as pd

# 샘플 데이터 생성
data = {
    '상품명': ['티셔츠', '스니커즈', '청바지', '러닝화'],
    '가격': [25990, 79990, 34990, 59990],
    '판매량': [100, 200, 150, 180],
    '인기도': [5, 4, 3, 2]
}
df = pd.DataFrame(data)

# 선택 옵션
options = ['판매순', '사이즈별 인기순', '출시일순',]
selected_option = st.selectbox("정렬 기준 선택:", options)

# 선택된 옵션에 따라 데이터 정렬
if selected_option == '인기순':
    sorted_df = df.sort_values(by='인기도', ascending=False)
elif selected_option == '판매순':
    sorted_df = df.sort_values(by='판매량', ascending=False)
elif selected_option == '오래된 상품순':
    sorted_df = df.sort_values(by='날짜', ascending=True)  # 날짜 컬럼이 없어서 임의로 추가한 것입니다.
else:  # 최근 상품순
    sorted_df = df.sort_values(by='날짜', ascending=False)  # 날짜 컬럼이 없어서 임의로 추가한 것입니다.

# 정렬된 데이터 출력
st.table(sorted_df)
