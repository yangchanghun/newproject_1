import csv
import streamlit as st

def csv_to_dict(csv_file_path):
    data = []
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

csv_file_path = '123.csv'
sales_data_dict = csv_to_dict(csv_file_path)

import pandas as pd

# CSV 파일을 DataFrame으로 읽어옵니다.
df = pd.read_csv('123.csv')

# 중복된 상품명을 제거하고 처음 나타난 행만 남깁니다.
unique_df = df.drop_duplicates(subset='상품명', keep='first')

# 결과를 출력합니다.
print(unique_df)
