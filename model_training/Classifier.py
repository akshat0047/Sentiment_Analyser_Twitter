import nltk


class PrepareClassifier:
    def __init__(self):
        word_features = []

    def buildVocabulary(self, preprocessedTrainingData):
        all_words = []

        for (words, sentiment) in preprocessedTrainingData:
            all_words.extend(words)

        wordlist = nltk.FreqDist(all_words)
        word_features = wordlist.keys()

        return word_features

    def extract_features(self, tweet):
        tweet_words = set(tweet)
        features = {}
        for word in self.word_features:
            features['contains(%s)' % word] = (word in tweet_words)
        return features

    # Getting the classifier ready to be trained

    def prepareFeatures(self, preprocessedTrainingData):
        self.word_features = self.buildVocabulary(preprocessedTrainingData)
        trainingFeatures = nltk.classify.apply_features(self.extract_features,
                                                        preprocessedTrainingData)
        return trainingFeatures
