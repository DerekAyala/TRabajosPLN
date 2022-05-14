import re

carpetaNombre = "textos/"
archivo = "texto1.txt"

with open(carpetaNombre+archivo,"r") as archivo:
  texto = archivo.read()

expresion_regular = re.compile(r"BWA")
expresion_regular2 = re.compile(r"im+")
resultados = expresion_regular.finditer(texto)
resultados2 = expresion_regular2.finditer(texto)

for resultado in resultados:
  print(resultado.group(0))

for resultado2 in resultados2:
  print(resultado2.group(0))
