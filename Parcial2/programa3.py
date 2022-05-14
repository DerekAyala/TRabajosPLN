from tkinter import simpledialog
import nltk
import matplotlib

archivo_nombre = "../textos/documento.txt"

with open(archivo_nombre,"r") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto, "spanish")


for token in tokens:
    print(token)

palabras_totales = len(tokens)
print("Palabras totales: ", palabras_totales)

print("---------------------------------------------------")

texto_nltk = nltk.Text(tokens)
distribucion = nltk.FreqDist(texto)

distribucion.plot()

print("---------------------------------------------------")

hapaxes = distribucion.hapaxes()

for hapax in hapaxes:
    print(hapax)
