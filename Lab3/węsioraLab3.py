import nltk
from nltk import ngrams, word_tokenize, re, Counter
from nltk.book import *
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.corpus import brown
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import wordnet as wn
from tabulate import tabulate


text_list = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
#---Zad1---
print("\nZad1")
print("Gutenberg filenames:" + str(nltk.corpus.gutenberg.fileids()))

#---Zad2---
print("\nZad2")
print("Inaugural filenames:" + str(nltk.corpus.inaugural.fileids()))

#---Zad3---
print("\nZad3")
print("Movie_reviews categories:" + str(nltk.corpus.movie_reviews.categories()))

#---Zad4---
print("\nZad4")
print("Inaugural sentences from \"1909-Taft.txt\":" + str(nltk.corpus.inaugural.sents(fileids=["1909-Taft.txt"])))

#---Zad5---
print("\nZad5")

text = brown.words(categories='adventure')
fdist = nltk.FreqDist(w.lower() for w in text)
words = ['mountains', 'ocean']
for w in words:
    print(w + ':' + str(fdist[w]), end=' ')

bigrams_freq = Counter(nltk.bigrams(text))
print ("bungee jump: " + str(bigrams_freq[('bungee', 'jump')]))

#---Zad6---
print("\nZad6")
fdist = nltk.FreqDist(nltk.corpus.inaugural.words())
for k,v in fdist.most_common(10):
    print (k,v)

#---Zad7---
print("\nZad7")
def non_stopword_percentage(text):
    stopwords = nltk.corpus.stopwords.words('english')
    non_stopwords = [w for w in text if w.lower() not in stopwords]
    fraction = len(non_stopwords) / len(text) * 100
    return "%.2f%%" % fraction
for text in text_list:
    print("Percentage of non-stopwords in " + str(text) + ": " + non_stopword_percentage(text))

#---Zad8---
print("\nZad8")
journalist = swn.senti_synset('journalist.n.01')
writer = swn.senti_synset('writer.n.01')
actor = swn.senti_synset('actor.n.01')
singer = swn.senti_synset('singer.n.01')
print(journalist)
print(writer)
print(actor)
print(singer)

#---Zad9---
print("\nZad9")
def compare(word1, word2):
    ws1 = wn.synsets(word1)[0]
    ws2 = wn.synsets(word2)[0]
    return (ws1.path_similarity(ws2))

word_pairs = [("boy", "lad"), ("journey", "voyage"), ("coast", "hill"), ("monk", "slave"), ("food", "fruit"), ("journey", "car")]

for x in word_pairs:
    print("Similarity of words " + str(x) + ": " + str(compare(x[0], x[1])))

#---Zad10---
print("\nZad10")
table = []
for t in nltk.corpus.gutenberg.fileids():
    avg_sentence_length= len(nltk.corpus.gutenberg.words(fileids=[t])) / len(nltk.corpus.gutenberg.sents(fileids=[t]))
    avg_word_length = sum(len(word) for word in gutenberg.words(fileids=[t])) / len(gutenberg.words(fileids=[t]))
    duplicate_avg=(len(gutenberg.words(fileids=[t]))/len(set(gutenberg.words(fileids=[t]))))
    table.append([str(t), str(avg_sentence_length), str(avg_word_length), str(duplicate_avg)])

print(tabulate(table, headers=['tekst', 'srednia dlugosc zdania', 'srednia dlugosc slowa', 'srednie duplikaty'], tablefmt='orgtbl'))

#---Zad11---
print("\nZad11")
tagged_words = nltk.corpus.brown.tagged_words(fileids= 'cr09', tagset='universal')
print(str(nltk.Counter([j for i,j in tagged_words])))