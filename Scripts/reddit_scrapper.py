import praw
from datetime import datetime
reddit = praw.Reddit(
    client_id =  "2XJioSzFpLOj12zHJq31RQ",
    client_secret = "fnIPbcUfEZl5-8YlwtSVEokoWOrJYg",
    user_agent="social_media_sentiment_project by u/Ok_Bag6920")

 
subreddit = reddit.subreddit("mentalhealth")
from datetime import datetime
data = [] 
for comment in subreddit.comments(limit= 10): 
     data.append({
        "text": comment.body,
        "user": str(comment.author)  
        ,"created_at": datetime.fromtimestamp(comment.created_utc)
   })

import pandas as pd

df = pd.DataFrame(data,columns=["text","user","created_at"])
df.to_csv("Reddit_comments.csv",index = False)