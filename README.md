# stock-market-sentiment-analysis
This program predicts if the stock price of a company will </br> increase or decrease based on top news headlines.

## About the data

Data set used - https://www.kaggle.com/aaron7sun/stocknews

The timeframe is from the 6th of August 2008 to the 1st of July 2016.

This data set consists of two csv files. </br>

'upload_DJIA_table.csv' file contains the information about the stock price.</br>

'Combined_News_DJIA.csv' file contains the news for each date. </br>
They are ranked by reddit users votes, and only the top 25 headlines are considered for a single date.

## Preparing the data

#### Getting the data

```
df1 = pd.read_csv('data/Combined_News_DJIA.csv')
df2 = pd.read_csv('data/upload_DJIA_table.csv')
```
#### Merge the data set on the data field
```
merge = df1.merge(df2, how='inner', on='Date')
```

#### Show an example headline



#### Clean the data
