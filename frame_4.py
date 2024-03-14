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

df = pd.read_csv('123.csv')

unique_df = df.drop_duplicates(subset='상품명', keep='first')


print(unique_df)
