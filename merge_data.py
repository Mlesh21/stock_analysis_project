

import pandas as pd
import os

folder = 'data'
all_data = []

for filename in os.listdir(folder):
    if filename.endswith('.csv'):
        filepath = os.path.join(folder, filename)

        with open(filepath, 'r') as f:
            first_line = f.readline().strip().split(',')
            for _ in range(2):
                f.readline()
            third_line = f.readline().strip().split(',')

        df = pd.read_csv(filepath, skiprows=3, header=None)

        new_columns = [third_line[0]] + first_line[1:]
        df.columns = new_columns

        # Переименовываем первую колонку в 'Date'
        df.rename(columns={df.columns[0]: 'Date'}, inplace=True)

        print(f"Файл: {filename} - колонки: {df.columns.tolist()}")

        ticker = filename.split('.')[0]
        df['Ticker'] = ticker

        df['Date'] = pd.to_datetime(df['Date'])

        all_data.append(df)

combined_df = pd.concat(all_data, ignore_index=True)
combined_df.to_csv('combined_stocks.csv', index=False)
print(combined_df.head())