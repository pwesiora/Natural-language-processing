import nltk
import matplotlib.pyplot as plt
from nltk.corpus import inaugural
import pyphen

names, num_words, num_sents, num_vocab, word1, word2, lexical_diversity, num_avg_words_per_sentence, \
    num_avg_vocab_per_sentence, num_avg_syl, num_hapaxes, avg_hapaxes, word_list = ([] for i in range(13))

symbols = [',', '.', ':', ';', "'", '(', ')', '"', '!', '!?', '?', '-']
stop_words = nltk.corpus.stopwords.words('english')
stop_words.extend(symbols)
stop_words = set(stop_words)
sylab_dict = pyphen.Pyphen(lang='en')


def get_syllables_count(text):
    n = 0
    for i in text:
        s = sylab_dict.inserted(i)
        n = n + 1 + s.count('-')
    return n


cfd = nltk.ConditionalFreqDist((target, fileid[:4])
                               for fileid in inaugural.fileids()
                               for w in inaugural.words(fileid)
                               for target in ['america', 'law', 'world', 'USA', 'US']
                               if w.lower().startswith(target))
plt.gcf().canvas.set_window_title("Word count 1")
cfd.plot()

cfd2 = nltk.ConditionalFreqDist((target, fileid[:4])
                                for fileid in inaugural.fileids()
                                for w in inaugural.words(fileid)
                                for target in ['unity', 'heal', 'together']
                                if w.lower().startswith(target))
plt.gcf().canvas.set_window_title("Word count 2")
cfd2.plot()

for fileid in inaugural.fileids():
    print(fileid)
    word_list = list(inaugural.words(fileid))
    for i in stop_words:
        if i in word_list:
            while i in word_list:
                word_list.remove(i)
    names.append(fileid[:4])
    # words = len(inaugural.words(fileid)) # wraz z słowami z stop listy
    words = len(word_list)  # bez słów z stop listy
    num_words.append(words)
    word_fdist = nltk.FreqDist(word_list)
    sents = len(inaugural.sents(fileid))
    num_sents.append(sents)
    vocab = len(set(w.lower() for w in word_list))
    num_vocab.append(vocab)
    hapaxes = len(word_fdist.hapaxes())
    num_hapaxes.append(hapaxes)
    avg_hapaxes.append(hapaxes / sents)
    lexical_diversity.append((vocab / words))
    num_avg_words_per_sentence.append(round(words / sents, 2))
    num_avg_vocab_per_sentence.append(round(vocab / sents, 2))
    avg_syl = get_syllables_count(word_list) / words
    num_avg_syl.append(avg_syl)

    word1.append(len(nltk.re.findall(r'(united states of america)', str.lower(inaugural.raw(fileid)))))
    word2.append(len(nltk.re.findall(r'(united states)(?!.*(of america))', str.lower(inaugural.raw(fileid)))))
    # print(len(nltk.re.findall(r'\b(U\.S\.A)\b', str(inaugural.raw(fileid)))))


def create_plot(x, xlabel, ylabel, title, y, l, y2='', l2='', y3='', l3=''):
    plt.figure(figsize=(9, 3))
    plt.rcParams['axes.facecolor'] = 'white'
    plt.rcParams['axes.edgecolor'] = 'white'
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.alpha'] = 1
    plt.rcParams['grid.color'] = "#cccccc"
    plt.grid(True)
    plt.xticks(rotation='vertical')
    plt.plot(x, y, label=l, linestyle='-', marker='o')
    if y2 != '':
        plt.plot(x, y2, label=l2,  linestyle='-', marker='o')
        if y3 != '':
            plt.plot(x, y3, label=l3,  linestyle='-', marker='o')
    plt.legend(loc='upper right')
    plt.gcf().canvas.set_window_title(title)
    plt.suptitle(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    return plt


create_plot(names, 'Rok', 'Liczba słów', 'Liczba słów w przemowie', num_words, 'Słowa', num_vocab, 'Unikatowe słowa',
            num_hapaxes, "Hapaksy").show()
create_plot(names, 'Rok', 'Liczba słów', 'Średnia liczba słów w zdaniu', num_avg_words_per_sentence, 'Słowa',
            num_avg_vocab_per_sentence, 'Unikatowe słowa', avg_hapaxes, "Hapaksy").show()
create_plot(names, 'Rok', 'Różnorodność', 'Różnorodność leksykalna', lexical_diversity,
            'Różnorodność leksykalna').show()
create_plot(names, 'Rok', 'Liczba zdań', 'Liczba zdań w przemowie', num_sents, 'Zdania').show()
create_plot(names, 'Rok', 'Liczba sylab', 'Średnia liczba sylab na słowo w przemowie', num_avg_syl,
            'Średnie sylaby').show()
create_plot(names, 'Rok', 'Ilość wystąpień', 'US vs USA', word1, 'United States of America', word2,
            'United States').show()
