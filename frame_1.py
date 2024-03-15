import csv
import streamlit as st
def csv_to_dict(csv_file_path):
    data = []
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

csv_file_path = '543.csv'
sales_data_dict = csv_to_dict(csv_file_path)

# 결과 출력





print(sales_data_dict)