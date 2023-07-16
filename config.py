import snscrape.modules.twitter as sntwitter
from itertools import islice

query = "organic food"  # Your search query
max_tweets = 100  # Maximum number of tweets to retrieve

tweets = islice(sntwitter.TwitterSearchScraper(query).get_items(), max_tweets)

for tweet in tweets:
    tweet_id = tweet.id
    username = tweet.user.username
    created_at = tweet.date
    text = tweet.content
    likes = tweet.likeCount
    retweets = tweet.retweetCount

    # Process or store the extracted information as needed
    print(f"Tweet ID: {tweet_id}")
    print(f"Username: {username}")
    print(f"Created At: {created_at}")
    print(f"Text: {text}")
    print(f"Likes: {likes}")
    print(f"Retweets: {retweets}")
    print("------")
