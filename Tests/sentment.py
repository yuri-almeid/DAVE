from nltk.classify import NaiveBayesClassifier
import nltk

# nltk.download('punkt')

def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})

pos = []
with open("./pos_tweets.txt") as f:
    for i in f: 
        pos.append([format_sentence(i), 'pos'])
 
neg = []
with open("./neg_tweets.txt") as f:
    for i in f: 
        neg.append([format_sentence(i), 'neg'])
 
# next, split labeled data into the training and test data
training = pos[:int((.8)*len(pos))] + neg[:int((.8)*len(neg))]
test = pos[int((.8)*len(pos)):] + neg[int((.8)*len(neg)):]


classifier = NaiveBayesClassifier.train(training)

while True:
    ex = input('Type something: ')

    sentiment = classifier.classify(format_sentence(ex))

    if sentiment == 'pos':
        print('Your sentiment is positive! :)')
    else:
        print('Your sentiment is negative! :(')
