import matplotlib.pyplot as plt
import streamlit as st
# 판매량 데이터를 둥근 차트로 시각화하는 함수
def visualize_sales(dataframe):
    # 데이터프레임에서 상품별 판매량 추출
    sales_count = dataframe['상품명'].value_counts()

    # 둥근 차트 생성
    fig, ax = plt.subplots()
    ax.pie(sales_count, labels=sales_count.index, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # 차트를 이미지로 변환하여 Streamlit에 표시
    st.pyplot(fig)