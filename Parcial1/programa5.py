from matplotlib.pyplot import text


carpetaNombre = "textos/"
archivoSalida= "textos.txt"

with open(carpetaNombre+archivoSalida,"r") as archivo:
  texto = archivo.read()

simbolos=["(",")",",",".",";",":","\""]

for simbolo in simbolos:
  texto = texto.replace(simbolo," "+ simbolo + " ")

palabras_lista = texto.split()

palabras_unica=[]

for palabra in palabras_lista:
  if palabra in palabras_unica:
    continue
  palabras_unica.append(palabra)

print(palabras_unica)
print("numero de palabras unicas en el documento:", len(palabras_unica))
print("numero de palabras en el documento:", len(palabras_lista))
