#Derek Moises Ayala

import nltk

print("Derek Moises Ayala")

archivo_nombre = "../textos/documento.txt"

with open(archivo_nombre, "r") as archivo:
    texto=archivo.read()

print("----------------------------------------------------")
palabras_funcionales = nltk.corpus.stopwords.words("spanish")
for palabras_funcional in palabras_funcionales:
    print(palabras_funcional)

tokens = nltk.word_tokenize(texto, "spanish")
token_limpios = []
for token in tokens:
    if token not in palabras_funcionales:
        token_limpios.append(token)

print(len(tokens))
print(len(token_limpios))
text_limpio_nltk = nltk.Text(token_limpios)
distribucion_limpia = nltk.FreqDist(text_limpio_nltk)
distribucion_limpia.plot(40)
