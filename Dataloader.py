# # Prices Dataloader

import yfinance as yf
data = yf.download(list(isin_ticker_dict.values()), '2018-01-01','2023-12-31',interval="1d")['Adj Close']
data['Date'] = pd.to_datetime(data.index)
data.set_index('Date', inplace=True)
data = data.reindex(pd.date_range(data.index.min(), data.index.max())).sort_index(ascending=True).reset_index().rename(columns={'index': 'Date'})
data.fillna(method = 'bfill', inplace = True)
data.rename(columns = ticker_isin_dict, inplace = True)

data.to_csv(r'C:\Users\mayan\OneDrive\Documents\PersonalFinance\MF_PRICES.csv', index = False)