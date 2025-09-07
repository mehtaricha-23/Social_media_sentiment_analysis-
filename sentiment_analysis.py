import pandas as pd
import numpy as np
import re
from wordcloud import WordCloud
from textblob import TextBlob

# Load the Twitter data
twitter_df =  pd.read_csv('tweeter_data.csv')


# Load the Youtube comments data
youtube_df = pd.read_csv('youtube_comments.csv')


# Load the Reddit comments data 
reddit_df = pd.read_csv('reddit_comments.csv')


print('twitter data',twitter_df.shape)
print('youtube data',youtube_df.shape)
print('reddit data', reddit_df.shape)

# Data Cleaning Fintion

def clean_text(text):
    text =str(text).lower()   # Lowercase
    text = re.sub(r'http\S+|www\s','',text)  # Remove URLs
    text = re.sub(r'@\w+|#\w+','',text)
    text = re.sub(r'[^a-z\s]','',text)  # Remove special characters and numbers
    text = re.sub(r'\s+', '',text).strip() # Remove extra whitespace
    return text

#Apply Cleaning
twitter_df['clean_text'] = twitter_df['text'].apply(clean_text)
youtube_df['clean_text'] = youtube_df['text'].apply(clean_text)
reddit_df['clean_text'] = reddit_df['text'].apply(clean_text)

 # Sentiment Analysis Function 
def get_Sentiment(text):
    analyser = TextBlob(text)
    if analyser.sentiment.polarity > 0:
        return 'Positive'
    elif analyser.sentiment.polarity <0 :
        return 'Negative'
    else : 
        return 'nuetral'
    
# Applt Sentiment Analysis

twitter_df['clean_text'] = twitter_df['text'].apply(get_Sentiment)
youtube_df['clean_text'] = youtube_df['text'].apply(get_Sentiment)
reddit_df['clean_text'] = reddit_df['text'].apply(get_Sentiment)

# Add Platfrom Column & Merge All Data
twitter_df['platfrom'] =  'Twitter'
youtube_df['platfrom'] =  'Youtube'
reddit_df['platfrom'] =   'Reddit'
# Combine all data



final_df = pd.concat([reddit_df, youtube_df, twitter_df], axis=0, ignore_index=True)

final_df.to_csv("social_media_sentiment.csv", index=False)
print(final_df.columns)
