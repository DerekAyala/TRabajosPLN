
import nltk

sentence = "../textos/documento.txt"

tokens = nltk.word_tokenize(sentence)


tagged = nltk.pos_tag(tokens)
tagged[0:6]


from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()
