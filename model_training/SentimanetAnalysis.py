import twitter
from dotenv import load_dotenv
import os
from Preprocessor import PreProcessTweets
from FetchTweets import buildTrainingSet

load_dotenv()

# Registering our keys
api = twitter.Api(consumer_key=os.getenv('CONSUMER_KEY'),
                  consumer_secret=os.getenv('CONSUMER_SECRET'),
                  access_token_key=os.getenv('ACCESS_TOKEN'),
                  access_token_secret=os.getenv('ACCESS_TOKEN_SECRET'))

# Testing the API
# print(api.VerifyCredentials())

# Method to build test dataset using a search term


def buildTestSet(search_key):
    try:
        tweets_fetched = api.GetSearch(search_key, count=100)
        print(str(len(tweets_fetched)) + " tweets for the term " + search_key)
        return [{"text": status.text, "label": None}
                for status in tweets_fetched]
    except:
        print("something went wrong..")
        return None


# Testing the search endpoint

'''
search_term = input("Enter a search keyword:")
testDataSet = buildTestSet(search_term)
print(testDataSet[0:4])
'''

# Building the training set

corpusFile = "./corpus.csv"
tweetDataFile = "./tweetDataFile.csv"
trainingData = buildTrainingSet(corpusFile, tweetDataFile)

# Preprocess the data

tweetProcessor = PreProcessTweets()
preprocessedTrainingSet = tweetProcessor.processTweets(trainingData)
preprocessedTestSet = tweetProcessor.processTweets(testDataSet)
