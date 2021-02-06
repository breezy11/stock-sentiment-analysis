# stock-market-sentiment-analysis
This program predicts if the stock price of a company will </br> increase or decrease based on top news headlines.

## About the data

Data set used - https://www.kaggle.com/aaron7sun/stocknews

The timeframe is from the 6th of August 2008 to the 1st of July 2016.

The stock used is Dow Jones Industrial Average (DJIA).

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

b"Georgia 'downs two Russian warplanes' as countries move to brink of war" b'BREAKING: Musharraf to be impeached.' b'Russia Today: Columns of troops roll into South Ossetia; footage from fighting (YouTube)' b'Russian tanks are moving towards the capital of South Ossetia, which has reportedly been completely destroyed by Georgian artillery fire' b"Afghan children raped with 'impunity,' U.N. official says - this is sick, a three year old was raped and they do nothing" b'150 Russian tanks have entered South Ossetia whilst Georgia shoots down two Russian jets.' b"Breaking: Georgia invades South Ossetia, Russia warned it would intervene on SO's side" b"The 'enemy combatent' trials are nothing but a sham: Salim Haman has been sentenced to 5 1/2 years, but will be kept longer anyway just because they feel like it." b'Georgian troops retreat from S. Osettain capital, presumably leaving several hundred people killed. [VIDEO]' b'Did the U.S. Prep Georgia for War with Russia?' b'Rice Gives Green Light for Israel to Attack Iran: Says U.S. has no veto over Israeli military ops' b'Announcing:Class Action Lawsuit on Behalf of American Public Against the FBI' b"So---Russia and Georgia are at war and the NYT's top story is opening ceremonies of the Olympics?  What a fucking disgrace and yet further proof of the decline of journalism." b"China tells Bush to stay out of other countries' affairs" b'Did World War III start today?' b'Georgia Invades South Ossetia - if Russia gets involved, will NATO absorb Georgia and unleash a full scale war?' b'Al-Qaeda Faces Islamist Backlash' b'Condoleezza Rice: "The US would not act to prevent an Israeli strike on Iran." Israeli Defense Minister Ehud Barak: "Israel is prepared for uncompromising victory in the case of military hostilities."' b'This is a busy day:  The European Union has approved new sanctions against Iran in protest at its nuclear programme.' b"Georgia will withdraw 1,000 soldiers from Iraq to help fight off Russian forces in Georgia's breakaway region of South Ossetia" b'Why the Pentagon Thinks Attacking Iran is a Bad Idea - US News &amp; World Report' b'Caucasus in crisis: Georgia invades South Ossetia' b'Indian shoe manufactory  - And again in a series of "you do not like your work?"' b'Visitors Suffering from Mental Illnesses Banned from Olympics' b"No Help for Mexico's Kidnapping Surge"

#### Clean the data

```
clean_headlines = []
for i in range(0, len(headlines)):
    clean_headlines.append(re.sub("b[(')]", '', headlines[i]))
    clean_headlines[i] = re.sub('b[(")]', '', clean_headlines[i])
    clean_headlines[i] = re.sub("\'", '', clean_headlines[i])
```

#### Show an example headline after cleaning

Georgia downs two Russian warplanes as countries move to brink of war" BREAKING: Musharraf to be impeached. Russia Today: Columns of troops roll into South Ossetia; footage from fighting (YouTube) Russian tanks are moving towards the capital of South Ossetia, which has reportedly been completely destroyed by Georgian artillery fire Afghan children raped with impunity, U.N. official says - this is sick, a three year old was raped and they do nothing" 150 Russian tanks have entered South Ossetia whilst Georgia shoots down two Russian jets. Breaking: Georgia invades South Ossetia, Russia warned it would intervene on SOs side" The enemy combatent trials are nothing but a sham: Salim Haman has been sentenced to 5 1/2 years, but will be kept longer anyway just because they feel like it." Georgian troops retreat from S. Osettain capital, presumably leaving several hundred people killed. [VIDEO] Did the U.S. Prep Georgia for War with Russia? Rice Gives Green Light for Israel to Attack Iran: Says U.S. has no veto over Israeli military ops Announcing:Class Action Lawsuit on Behalf of American Public Against the FBI So---Russia and Georgia are at war and the NYTs top story is opening ceremonies of the Olympics?  What a fucking disgrace and yet further proof of the decline of journalism." China tells Bush to stay out of other countries affairs" Did World War III start today? Georgia Invades South Ossetia - if Russia gets involved, will NATO absorb Georgia and unleash a full scale war? Al-Qaeda Faces Islamist Backlash Condoleezza Rice: "The US would not act to prevent an Israeli strike on Iran." Israeli Defense Minister Ehud Barak: "Israel is prepared for uncompromising victory in the case of military hostilities." This is a busy day:  The European Union has approved new sanctions against Iran in protest at its nuclear programme. Georgia will withdraw 1,000 soldiers from Iraq to help fight off Russian forces in Georgias breakaway region of South Ossetia" Why the Pentagon Thinks Attacking Iran is a Bad Idea - US News &amp; World Report Caucasus in crisis: Georgia invades South Ossetia Indian shoe manufactory  - And again in a series of "you do not like your work?" Visitors Suffering from Mental Illnesses Banned from Olympics No Help for Mexicos Kidnapping Surge"
