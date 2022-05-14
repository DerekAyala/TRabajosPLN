from distutils import archive_util
import nltk

documento = "../textos/documento.txt"

with open(documento, "r") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto,"spanish")
for token in tokens:
    print(token)

palabras_total = len(tokens)
print("Palabras",palabras_total)

total_conjunto = set(tokens)
palabras_diferentes = len(total_conjunto)
print("Palabras diferentes ", palabras_diferentes)

riqueza_lexica = palabras_diferentes/palabras_total
print("Riqueza lexica : ", riqueza_lexica)
riqueza_lexicap = 100* riqueza_lexica
print("Porcentaje de riqueza lexica: ", round(riqueza_lexicap, 2),"%")

conteo_individual = tokens.count("BWA")

print("Numero de veces que se encuentra la palabra: ", conteo_individual)

palabras_totales = len(tokens)

porcentaje = 100 * conteo_individual/palabras_totales
porcentaje = round(porcentaje, 2)
print(porcentaje,"%")

texto_nltk = nltk.Text(tokens)
texto_nltk.concordance("datos")
print("------------------------------------")
texto_nltk.similar("datos")
