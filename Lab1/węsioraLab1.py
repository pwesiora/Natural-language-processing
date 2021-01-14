#import nltk
#nltk.download()
import nltk
from tabulate import tabulate
from nltk.book import *

text_list = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
#---Zad1---
print("\nZad1")
print(text1)
print("blue: " + str(text1.count("blue")))
print("sea: " + str(text1.count("sea")))
print("common contexts: ")
text1.common_contexts(["blue", "sea"])
print ("\n")

print(text2)
print("speak: " + str(text2.count("speak")))
print("word: " + str(text2.count("word")))
print("common contexts: ")
text2.common_contexts(["speak", "word"])
print ("\n")

print(text3)
print("fruit: " + str(text3.count("fruit")))
print("good: " + str(text3.count("good")))
print("common contexts: ")
text3.common_contexts(["fruit", "good"])
print ("\n")

print(text4)
print("good: " + str(text4.count("good")))
print("person: " + str(text4.count("person")))
print("common contexts: ")
text4.common_contexts(["good", "person"])
print ("\n")

print(text5)
print("kind: " + str(text5.count("kind")))
print("face: " + str(text5.count("face")))
print("common contexts: ")
text5.common_contexts(["kind", "face"])
print ("\n")

print(text6)
print("grail: " + str(text6.count("grail")))
print("king: " + str(text6.count("king")))
print("common contexts: ")
text6.common_contexts(["grail", "king"])
print ("\n")

print(text7)
print("low: " + str(text7.count("low")))
print("price: " + str(text7.count("price")))
print("common contexts: ")
text7.common_contexts(["low", "price"])
print ("\n")

print(text8)
print("good: " + str(text8.count("good")))
print("day: " + str(text8.count("day")))
print("common contexts: ")
text8.common_contexts(["good", "day"])
print ("\n")

print(text9)
print("difference: " + str(text9.count("difference")))
print("significant: " + str(text9.count("significant")))
print("common contexts: ")
text9.common_contexts(["difference", "significant"])
print ("\n")

#---Zad2---
print("\nZad2")
count=1
table = []
for i in text_list:
    table.append(["text" + str(count), str(len(i)), str(len(set(i))), str(len(i) / len(set(i)))])
    count=count+1
print(tabulate(table, headers= ['tekst','liczba słów', 'słowa różne', 'lexical_diversity'], tablefmt='orgtbl'))

#---Zad3---
print("\nZad3")
fdist1 = FreqDist(text1)
four_length_text1 = sorted(w for w in set(text1) if len(w) == 4 and fdist1[w] == 4)
print(four_length_text1)
print("number of four letter words: " + str(len(four_length_text1)))

#---Zad4---
print("\nZad4")
long_word_text1 = sorted(w for w in set(text1) if len(w) > 17 and fdist1[w] > 17)
print(long_word_text1)
print("number of words with more than seventeen letters: " + str(len(long_word_text1)))

#---Zad5---
print("\nZad5")
dict1 = sorted(set(sent1))
dict2 = sorted(set(sent2))
dict3 = sorted(set(sent3))
dict4 = sorted(set(sent4))
dict5 = sorted(set(sent5))
dict6 = sorted(set(sent6))
dict7 = sorted(set(sent7))
dict8 = sorted(set(sent8))
dict_all = sorted(set(dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8))
print(dict_all)

#---Zad6---
print("\nZad6")
def VocabSize(data):
    return len(set(data))
for i in text_list:
    print(str(i)+":")
    print (VocabSize(i))

#---Zad7---
print("\nZad7")
most_freq = nltk.FreqDist(text1)
print(most_freq.most_common(10))

#---Zad8---
print("\nZad8")
def find_longest(text):
    longest = "ERROR"
    for word in text:
        if len(word) > len(longest):
            longest = word
    return longest
for i in text_list:
    print(str(i)+":")
    print(find_longest(i))
