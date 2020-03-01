import random

with open("tweets.txt", "r") as f:
    tweets = f.readlines()
    random.shuffle(tweets)

    train_index = (len(tweets) // 10) * 6
    test_index = train_index + (len(tweets) // 10) * 2
    valid_index = test_index + (len(tweets) // 10) * 2

    with open("tweets_train.txt", "w") as train:
        for tweet in tweets[:train_index]:
            train.write(tweet)

    with open("tweets_test.txt", "w") as test:
        for tweet in tweets[train_index:test_index]:
            test.write(tweet)

    with open("tweets_valid.txt", "w") as valid:
        for tweet in tweets[test_index:valid_index]:
            valid.write(tweet)