import tweepy

consumer_key = "vcuuvdDzlJPLLrEChTu02i84C";


consumer_secret = "CVgzafa3en4bN3WyxDiDcAZgBeVdxwCQD9LwHtdVgNJrsbUwJE";


access_token = "89472702-tytx3xBrubnsLYSj74JEWWfU3zhPuP9jmZ0nWildl";
access_token_secret = "184TRzX1vg6LvSR5orbkhyYXPoynN4F4cYLERlgUJYuPP";

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


