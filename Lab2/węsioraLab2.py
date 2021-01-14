import nltk
from nltk import ngrams, word_tokenize, re
from nltk.book import *
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.corpus import brown

text_list = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
tagged_sent_list = brown.tagged_sents()
#---Zad1---
print("\nZad1")
bigrm = nltk.bigrams(text5.tokens)
#print(len(list(nltk.bigrams(text5.tokens))))

print("\n10 most common bigrams:")
fdist = nltk.FreqDist(bigrm)
for k,v in fdist.most_common(10):
    print (k,v)

print("\n10 most common words:")
fdist = nltk.FreqDist(text5)
for k,v in fdist.most_common(10):
    print (k,v)

#---Zad2---
print("\nZad2")
ngram_count_list= []

def create_ngram_list(text, n):
    n_grams = ngrams(text, n)
    return [grams for grams in n_grams]
for i in range(3,7):
    print("\n" + str(i) + "-grams:")
    ngram_count= len(create_ngram_list(text5, i))
    print(ngram_count)
    ngram_count_list.append(ngram_count)

#---Zad3---
names = ['3-gram', '4-gram', '5-gram', '6-gram']
plt.figure(figsize=(9, 3))
plt.bar(names, ngram_count_list)
plt.ylim((45000,45010))
#Please uncomment to view graph
#plt.show()

#---Zad4---
print("\nZad4")
print("Words containing 'ing':")
print(re.findall(r'\b(\w+ing)\b', str(text1.tokens)))
print("Number of vowels:", end='')
print(len(re.findall(r'[aeiou]', str(text2.tokens))))
print("Number of 'U.S.A' occurrences':", end='')
print(len(re.findall(r'\b(U\.S\.A)\b', str(text4.tokens))))

#---Zad5---
print("\nZad5")
def non_stopword_percentage(text):
    stopwords = nltk.corpus.stopwords.words('english')
    non_stopwords = [w for w in text if w.lower() not in stopwords]
    fraction = len(non_stopwords) / len(text) * 100
    return "%.2f%%" % fraction
for text in text_list:
    print("Percentage of non-stopwords in " + str(text) + ": " + non_stopword_percentage(text))

#---Zad6---
print("\nZad6")
def verb_TO_verb(text):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(text):
        if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')):
            print (w1, w2, w3)
        #else:
            #print("Error: no verb-TO-verb found")
#for sent in sent_list:
#    token_sent = nltk.word_tokenize(str(sent))
#    tagged_sent = nltk.pos_tag(token_sent)
#    for s in tagged_sent:
#        verb_TO_verb(s)

for s in tagged_sent_list[:5]:
    verb_TO_verb(s)

#for s in tagged_sent_list[:50]:
#    verb_TO_verb(s)