def buildTrainingSet(corpusFile, tweetDataFile):
    import csv
    import time

    corpus = []

    with open(corpusFile, 'rt') as csvfile:
        lineReader = csv.reader(csvfile, delimiter=',', quotechar="\"")
        for row in lineReader:
            corpus.append({"tweet_id": row[2], "label": row[1],
                           "topic": row[0]})

    rate_limit = 180
    sleep_time = 900/180

    trainingDataSet = []

    for tweet in corpus:
        try:
            status = api.GetStatus(tweet["tweet_id"])
            print("Tweet fetched" + status.text)
            tweet["text"] = status.text
            trainingDataSet.append(tweet)
            time.sleep(sleep_time)

        except: 
            continue

    # Writing tweets to CSV File

    with open(tweetDataFile, 'wt') as csvfile:
        linewriter = csv.writer(csvfile, delimiter=',', quotechar="\"")
        for tweet in trainingDataSet:
            try:
                linewriter.writerow([tweet["tweet_id"], tweet["text"],
                                     tweet["label"], tweet["topic"]])
            except Exception as e:
                print(e)
    return trainingDataSet
