import nltk

archivo_nombre = "../textos/documento.txt"

with open(archivo_nombre,"r") as archivo:
  texto = archivo.read()

tokens = nltk.word_tokenize(texto,"spanish")
for token in tokens:
  print(token)

palabras_totales = len(tokens)

print("Numero de palabras: ",palabras_totales)

tokens_diferentes = set(tokens)
palabras_diferentes = len(tokens_diferentes)

print("Numero de palabras diferentes: ",palabras_diferentes)

riqueza = palabras_diferentes/palabras_totales
print("riqueza lexica: ", riqueza)
riqueza_cap = 100*palabras_diferentes/palabras_totales
print("Riqueza lexica: ",riqueza_cap)

texto_nlkt = nltk.Text(tokens)
palabra = input("ingrese una palabra: ")
texto_nlkt.concordance(palabra)
print("--------------------")
texto_nlkt.similar(palabra)
