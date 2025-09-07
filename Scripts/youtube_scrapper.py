from youtube_comment_downloader import YoutubeCommentDownloader
downloader = YoutubeCommentDownloader()
comments = downloader.get_comments_from_url("https://www.youtube.com/watch?v=rj7lh97z7JM")

data = []

for comment in comments:
    
    data.append({
        "user": comment.get('author'),
        "text": comment.get('text'),
        "created_at": comment.get('time_parsed')  # proper datetime
    })


import pandas as pd
df= pd.DataFrame(data, columns=['user','text',"created_at"])
df["created_at"] = pd.to_datetime(df["created_at"], unit="s", errors="coerce")

df.to_csv('youtube_comments.csv', index=False)   
