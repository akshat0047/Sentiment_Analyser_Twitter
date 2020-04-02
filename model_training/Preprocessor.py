import re
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords


class PreProcessTweets:
    def __init__(self):
        self._stopwords = set(stopwords.words('english') +
                              list(punctuation) + ['AT_USER', 'URL'])

    def processTweets(self, list_of_tweets):
        processedTweets = []
        for tweet in list_of_tweets:
            processedTweets.append((self._processTweet(tweet["text"]),
                                    tweet["label"]))
        return processedTweets

    def _processTweet(self, tweet):

        # convert text to lower-case
        tweet = tweet.lower()

        # Remove URLs
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)

        # Remove usernames
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet)

        # Remove the # in #hashtag
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)

        # Remove repeated characters (hellooo into hello)
        tweet = word_tokenize(tweet)
        return [word for word in tweet if word not in self._stopwords]
