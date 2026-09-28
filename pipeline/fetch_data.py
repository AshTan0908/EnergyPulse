import pandas as pd
import requests
import csv
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

url = "https://api.eia.gov/v2/petroleum/pri/spt/data/?frequency=weekly&data[0]=value&start=2020-01-01&end=2026-05-01&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000"
load_dotenv()
API_KEY = os.getenv("EIA_API_KEY")

params = {"api_key": API_KEY}

r = requests.get(url, params=params)
data = r.json()
#print(data)

df = pd.DataFrame(data['response']['data'])
#print(df)

c_data = df[['period', 'series-description', 'value', 'units']]
print(c_data['series-description'].unique())

pivot_df = df.pivot_table(
    index='period',
    columns='series-description',
    values='value',
    aggfunc='first'
).reset_index()

pivot_df['period'] = pd.to_datetime(pivot_df['period'])
pivot_df = pivot_df.sort_values('period')
#print(pivot_df.head(10))

'''
pivot_df.index = pd.to_datetime(pivot_df.index)

pivot_df = pivot_df.apply(pd.to_numeric, errors='coerce')

pivot_df = pivot_df.dropna(how='all')

fig, ax = plt.subplots(figsize=(16, 9))

for column in pivot_df.columns:
    ax.plot(
        pivot_df.index.to_pydatetime(),   
        pivot_df[column],
        label=column,
        linewidth=2
    )

ax.set_title('Oil Prices Over Time', fontsize=18)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Price', fontsize=14)

plt.xticks(rotation=45)
ax.grid(True)

ax.legend(
    bbox_to_anchor=(1.02, 1),
    loc='upper left',
    fontsize=8
)

plt.tight_layout()
plt.savefig('oil_prices_line_graph.png', dpi=300)

plt.show()

with open('crude_spot_prices.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(list(pivot_df.columns))
    for index, row in pivot_df.iterrows():
        writer.writerow(row.tolist())




plot_df = pivot_df.set_index('period')
plot_df.plot(figsize=(14, 8), linewidth=1.5)
plt.title('Price Change by Series Description')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(title='Series Description', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.grid(True)
plt.savefig('series_price_change.png', dpi=150)
plt.show()

brent_data.columns = ['Original Index', 'Date', 'Price ($/bbl)']
print(brent_data[brent_data['Price ($/bbl)']== brent_data['Price ($/bbl)'].max()])
'''