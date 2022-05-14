
archivo_nombre = "texto3.txt"

palabra = input("Escribe la palabra a buscar en el documento: \n")

with open(archivo_nombre,"r") as archivo:
  texto = archivo.read()

if palabra in texto:
  print("el documento tiene la palabra", palabra)
else:
  print("No esta ninguna de las anteriores")
