import os

carpetaNombre = "textos/"
archivoSalida= "textos.txt"

archivo_lista = os.listdir(carpetaNombre)

union = ""
for archivo_nombre in archivo_lista:
  archivo = open(carpetaNombre+archivo_nombre)
  texto = archivo.read()
  archivo.close()
  union+=texto

with open(carpetaNombre+archivoSalida,"w") as salida:
  salida.write(union)
  salida.close()
