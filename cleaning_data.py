import pandas as pd
df = pd.read_csv('combined_stocks.csv')
#print(df.isnull().sum())


df['Daily_return'] = df['Close'].pct_change()
profit_df = (df.sort_values(['Ticker', 'Date'])
             .groupby('Ticker')
             .agg(start_price = ('Close', 'first'), end_price = ('Close', 'last'))
             )
profit_df['Total_return'] = (profit_df['end_price']-profit_df['start_price'])
profit_df['Total_return (%)'] = (profit_df['end_price']-profit_df['start_price'])/profit_df['start_price']*100
profit_df = profit_df.reset_index()
df = df.merge(profit_df[['Ticker', 'Total_return', 'Total_return (%)']], on='Ticker', how='left')
df.to_csv('combined_stocks.csv', index=False)



