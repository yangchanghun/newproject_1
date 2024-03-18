import streamlit as st
import pandas as pd

# 전역으로 데이터프레임 선언
df = None

def load_csv_data(csv_file_path):
    # CSV 파일을 데이터프레임으로 변환
    global df
    df = pd.read_csv(csv_file_path)

def save_to_csv(dataframe, csv_file_path):
    # 데이터프레임을 CSV 파일로 저장
    dataframe.to_csv(csv_file_path, index=False)

def main():
    st.title('새로운 판매 기록 추가')

    global df  # 전역 데이터프레임을 사용

    # CSV 파일 업로드
    uploaded_file = st.file_uploader("CSV 파일 업로드", type=['csv'])
    if uploaded_file is not None:
        # 업로드한 CSV 파일을 데이터프레임으로 변환
        load_csv_data(uploaded_file)

    if df is not None:  # 데이터프레임이 존재하는 경우에만 실행
        # 사용자로부터 판매할 상품 선택
        product_options = df['상품명'].unique()
        selected_product = st.selectbox('상품 선택', product_options)

        # 선택한 상품의 정보 표시
        selected_product_info = df[df['상품명'] == selected_product].iloc[0]
        st.write(f"상품명: {selected_product}")
        st.write(f"가격: {selected_product_info['가격']}")
        st.write(f"출시날짜: {selected_product_info['출시날짜']}")

        # 해당 상품의 분류에 따라 사이즈 옵션 동적으로 표시
        category_options = df[df['상품명'] == selected_product]['분류'].unique()
        if len(category_options) == 1:
            selected_category = category_options[0]
        else:
            selected_category = st.selectbox('분류', category_options)

        # 선택한 분류에 해당하는 사이즈 옵션 표시
        sizes = df[(df['상품명'] == selected_product) & (df['분류'] == selected_category)]['사이즈'].unique()
        selected_size = st.selectbox('사이즈', sizes)

        # 사용자로부터 판매 기록 입력 받기
        gender = st.selectbox('성별', ['남성', '여성'])
        sale_date = st.date_input('판매날짜')

        # 사용자가 입력한 정보를 확인하고 처리하는 부분
        if st.button('판매 기록 추가'):
            new_record = pd.DataFrame({
                '상품명': [selected_product],
                '분류': [selected_category],
                '가격': [selected_product_info['가격']],
                '출시날짜': [selected_product_info['출시날짜']],
                '사이즈': [selected_size],
                '성별': [gender],
                '판매날짜': [sale_date]
            })
            # 새로운 판매 기록을 데이터프레임에 추가
            df = pd.concat([df, new_record], ignore_index=True)
            st.write('새로운 판매 기록이 추가되었습니다.')

            # 업데이트된 데이터프레임을 다시 CSV 파일로 저장
            save_to_csv(df, 'updated_data.csv')

            # 추가된 기록을 기반으로 통계 다시 계산
            st.title('판매 통계')
            st.write(df)  # 업데이트된 데이터프레임 출력
            # 여기에 추가적인 통계 및 시각화 코드를 작성하여 업데이트된 통계를 표시

if __name__ == "__main__":
    main()
