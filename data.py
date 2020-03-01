import twitter
api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

screen_names = ["paulg", "isosteph", "eileentso", "guykawasaki", "christine", "bhorowitz", "peterfenton", "pmarca", "joshk", "reidhoffman", "sama", "mwseibel"]

for screen_name in screen_names:
  timeline = api.GetUserTimeline(screen_name=screen_name, count=500)
  earliest_tweet = min(timeline, key=lambda x: x.id).id
  print("getting tweets before:", earliest_tweet)

  while True:
      tweets = api.GetUserTimeline(
          screen_name=screen_name, max_id=earliest_tweet, count=500
      )
      new_earliest = min(tweets, key=lambda x: x.id).id

      if not tweets or new_earliest == earliest_tweet:
          break
      else:
          earliest_tweet = new_earliest
          print("getting tweets before:", earliest_tweet)
          timeline += tweets


  corpus = ""

  tweets = [tweet.text for tweet in timeline if tweet.text[:2] != "RT" and tweet.text[0] != "@"]

  for tweet in tweets:
    tokens = tweet.split()
    corpus += "\{}- ".format(screen_name)
    for token in tokens:
      if token[:4] != "http" and token[:5] != "https":
        corpus += token + " "
    corpus += "\n"

  with open("tweets.txt", "a") as f:
      f.write(corpus)