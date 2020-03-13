def GenderIdentify():
    # importing libraries
    # https://www.geeksforgeeks.org/python-gender-identification-by-name-using-nltk/

    import random
    from nltk.corpus import names
    import nltk

    def gender_features(word):
        return {'last_letter': word[-1]}

        # preparing a list of examples and corresponding class labels.

    labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                     [(name, 'female') for name in names.words('female.txt')])

    random.shuffle(labeled_names)

    # we use the feature extractor to process the names data.
    featuresets = [(gender_features(n), gender)
                   for (n, gender) in labeled_names]

    # Divide the resulting list of feature
    # sets into a training set and a test set.
    train_set, test_set = featuresets[500:], featuresets[:500]

    # The training set is used to
    # train a new "naive Bayes" classifier.
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    #print(classifier.classify(gender_features('mahavir')))

    # output should be 'male'
  #  print(nltk.classify.accuracy(classifier, train_set))
    print('Trained Gender Identify')
    # it shows accurancy of our classifier and
    # train_set. which must be more than 99 %
    # classifier.show_most_informative_features(10)
    return classifier