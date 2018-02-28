import pickle
from extractor import *

datasetFull = SimFinDataset('simfin-data.csv','semicolon')

with open('datasetFull.pkl', 'wb') as output:
    pickle.dump(datasetFull, output, pickle.HIGHEST_PROTOCOL)
	
companies = []
tickers = []
for i in range(len(datasetFull.companies)):
    companies.append(datasetFull.companies[i].name)
    tickers.append(datasetFull.companies[i].ticker)

ticker_company_df = pd.DataFrame({'Ticker Symbol':tickers, 'Company Name':companies})
ticker_company_df.to_csv('Ticker_Company.csv')