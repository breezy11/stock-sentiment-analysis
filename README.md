# stock-sentiment-analysis
This program predicts if the stock price of a company will increase or decrease based on top news headlines. <br>
Predictions are based on sentiment scores. The headlines are fed as blocks of texts to TextBlob to get the subjectivity and polarity scores. <br>

## data

Data set used - https://www.kaggle.com/aaron7sun/stocknews

The timeframe is from the 6th of August 2008 to the 1st of July 2016.

The stock used is Dow Jones Industrial Average (DJIA).

This data set consists of two csv files. </br>

'value.csv' file contains the information about the stock price.</br>

'combined-news' file contains the news for each date and a label that tracks what direction the stock went. </br>
"1" when DJIA Adj Close value rose or stayed as the same. </br>
"0" when DJIA Adj Close value decreased. </br>
The news are ranked by reddit users votes, and only the top 25 headlines are considered for a single date.


## model metrics

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| 0            | 0.56      | 0.20   | 0.29     | 193     |
| 1            | 0.53      | 0.85   | 0.65     | 205     |
| accuracy      |           |        | 0.54     | 398     |
| macro avg    | 0.54      | 0.53   | 0.47     | 398     |
| weighted avg | 0.54      | 0.54   | 0.48     | 398     |
