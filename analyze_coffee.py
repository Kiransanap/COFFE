
import pandas as pd
df = pd.read_csv('coffee_sales.csv', parse_dates=['date'])
print('Loaded', len(df), 'rows')
print(df.head())
# Example: total revenue by city
print('\nTotal revenue by city:\n', df.groupby('city')['revenue'].sum().sort_values(ascending=False))
