# Imports

import pandas as pd
import numpy as np
from textblob import TextBlob
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Load the data
df1 = pd.read_csv('data/Combined_News_DJIA.csv')
df2 = pd.read_csv('data/upload_DJIA_table.csv')

# Merge the data set on the data field
merge = df1.merge(df2, how='inner', on='Date')

# Show the merged data set
# print(merge)

# Combine the top news headlines
headlines = []

for row in range(0, len(merge.index)):
    headlines.append(' '.join(str(x) for x in merge.iloc[row, 2:27]))

# Print a sample of the combined headlines
# print(headlines[0])

# Clean the data
clean_headlines = []

# remove b', b" and \'
for i in range(0, len(headlines)):
    clean_headlines.append(re.sub("b[(')]", '', headlines[i]))
    clean_headlines[i] = re.sub('b[(")]', '', clean_headlines[i])
    clean_headlines[i] = re.sub("\'", '', clean_headlines[i])

# Add the clean headlines to the merge data set
merge['Combined News'] = clean_headlines

# Show the new column
# print(merge['Combined News'][0])

# Create a function to get the subjectivity
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

# Create a funtion to get the polarity
def getPolarity(text):
    return TextBlob(text).sentiment.polarity

# Create two new columns 'Subjectivity' and 'Polarity'
merge['Subjectivity'] = merge['Combined News'].apply(getSubjectivity)
merge['Polarity'] = merge['Combined News'].apply(getPolarity)

# Show the first 5 columns in the merge data set
# print(merge.head(3))

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

for i in range(0 , len(merge['Combined News'])):
    SIA = getSIA(merge['Combined News'][i])
    compound.append(SIA['compound'])
    neg.append(SIA['neg'])
    neu.append(SIA['neu'])
    pos.append(SIA['pos'])

# Store the sentiment scores in the merge data set
merge['Compound'] = compound
merge['Negative'] = neg
merge['Neutral'] = neu
merge['Positive'] = pos

# Show the merge data
# print(merge)

# Create a list of columns to keep
keep_columns = ['Open','High','Low','Volume','Subjectivity', 'Polarity', 'Compound', 'Negative', 'Neutral', 'Positive', 'Label']

# Data set used to determine whether the price will increase or decrease
df = merge[keep_columns]

# Show the data set
# print(df)

# Create the future data set
X = df
X = np.array(X.drop(['Label'], 1))

# Create the target data set
y = np.array(df['Label'])

# Split the data into training and test data
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create and train the model
model = LinearDiscriminantAnalysis().fit(x_train, y_train)

# Predict
predictions = model.predict(x_test)

# Show the model metrics
print(classification_report(y_test, predictions))