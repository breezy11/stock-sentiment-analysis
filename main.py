# Imports
import os
import pandas as pd
import numpy as np
from textblob import TextBlob
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Load data
news = pd.read_csv(os.path.join('Data','combined-news.csv'))
price = pd.read_csv(os.path.join('Data','value.csv'))

# Merge the data
data = news.merge(price, on='Date')

# Shifting the labels by -1 because the label and news were stored with the tomorrow's date
data['new-label'] = data['Label'].shift(-1).fillna(0).astype(int)

# Show the first 15 rows of selected columns
print(data[['Date','Open','Close','Adj Close','Label','new-label']].head(15))


# Combine the top news headlines
headlines = []

for row in range(0, len(data.index)):
    headlines.append(' '.join(str(x) for x in data.iloc[row, 2:27]))

# Print a sample of the combined headlines
# print(headlines[0])

# Clean the data
clean_headlines = []

# remove b', b" and \'
for i in range(0, len(headlines)):
    clean_headlines.append(re.sub("b[(')]", '', headlines[i]))
    clean_headlines[i] = re.sub('b[(")]', '', clean_headlines[i])
    clean_headlines[i] = re.sub("\'", '', clean_headlines[i])

# Add the clean headlines to the data set
data['Combined News'] = clean_headlines

# Show the new column
# print(data['Combined News'][0])

# Create a function to get the subjectivity
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

# Create a funtion to get the polarity
def getPolarity(text):
    return TextBlob(text).sentiment.polarity

# Create two new columns 'Subjectivity' and 'Polarity'
data['Subjectivity'] = data['Combined News'].apply(getSubjectivity)
data['Polarity'] = data['Combined News'].apply(getPolarity)

# Show the first 5 columns in the data set
# print(data.head(3))

# Create a function to get the sentiment scores
def getSIA(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment

# Get the sentiment scores for each day
compound = []
neg = []
pos = []
neu = []
SIA = 0

for i in range(0 , len(data['Combined News'])):
    SIA = getSIA(data['Combined News'][i])
    compound.append(SIA['compound'])
    neg.append(SIA['neg'])
    neu.append(SIA['neu'])
    pos.append(SIA['pos'])

# Store the sentiment scores in the data set
data['Compound'] = compound
data['Negative'] = neg
data['Neutral'] = neu
data['Positive'] = pos

# Show the
# data
# print(data)

# Create a list of columns to keep
keep_columns = ['Open','High','Low','Volume','Subjectivity', 'Polarity', 'Compound', 'Negative', 'Neutral', 'Positive', 'new-label']

# Data set used to determine whether the price will increase or decrease
df = data[keep_columns]

# Show the data set
# print(df)

# Create the future data set
X = df
X = np.array(X.drop(['new-label'], 1))

# Create the target data set
y = np.array(df['new-label'])

# Split the data into training and test data
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# Create and train the model
model = LinearDiscriminantAnalysis().fit(x_train, y_train)

# Predict
predictions = model.predict(x_test)

# Show the model metrics
print(classification_report(y_test, predictions))