import tweepy
import pandas as pd

client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAPCU3wEAAAAAPCbYvZ9CnXZLuXpY5IOIDZvjO9w%3Djw9rY591CgM6PwMN5CkZHs85SlDtP1lGPW0UQEGQbEVcXIaAuk")
query = "mental health OR depression OR anxiety -is:retweet lang:en"

try:
    tweets = client.search_recent_tweets(
        query=query,
        max_results=6,
        tweet_fields=["user","id", "text", "created_at", "lang","author"]
    )

    data = []
    if tweets.data:
        for tweet in tweets.data:
            data.append({
                "user" : tweet.author,
                "id": tweet.id,
                "text": tweet.text,
                "created_at": tweet.created_at,
                "author": tweet.author,
                "lang": tweet.lang
            })

        df = pd.DataFrame(data)
        df.to_csv("tweeter_data.csv", index=False, encoding="utf-8")
        print(" Saved tweeter_data.csv")
    else:
        print(" No tweets found. Query might not match recent tweets.")

except tweepy.errors.Unauthorized:
    print(" Bearer token invalid or expired. Please regenerate and update it.")
except tweepy.errors.TooManyRequests:
    print(" Rate limit exceeded. Please wait a few minutes and try again.")
except Exception as e:
    print(f" Some other error: {e}")
