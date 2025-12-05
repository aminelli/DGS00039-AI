import nltk
import nltk.sentiment.sentiment_analyzer
import nltk.sentiment.util
# Analysing for single words


def OneWord():
    positive_words = ['good', 'progress', 'luck']
    text = 'Hard Work brings progress and good luck.'.split()
    analysis = nltk.sentiment.util.extract_unigram_feats(text, positive_words)
    print(' ** Sentiment with one word **\n')
    print(analysis)

# Analysing for a pair of words


def WithBigrams():
    word_sets = [('Regular', 'fit'), ('fit', 'fine')]
    text = 'Regular excercise makes you fit and fine'.split()
    analysis = nltk.sentiment.util.extract_bigram_feats(text, word_sets)
    print('\n*** Sentiment with bigrams ***\n')
    print(analysis)

# Analysing the negation words.


def NegativeWord():
    text = 'Lack of good health can not bring success to students'.split()
    analysis = nltk.sentiment.util.mark_negation(text)
    print('\n**Sentiment with Negative words**\n')
    print(analysis)


OneWord()
WithBigrams()
NegativeWord()
