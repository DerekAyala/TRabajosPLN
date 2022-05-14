import os

carpetaNombre = "Tarea/textos/"
archivoSalida= "documento.txt"

archivos = os.listdir(carpetaNombre)
simbolos=["(",")",",",".",";",":","\"","¿","?","%"]

union = ""

for archivo_nombre in archivos:
  archivo = open(carpetaNombre+archivo_nombre)
  texto = archivo.read()
  archivo.close()
  union+=texto

with open(carpetaNombre+archivoSalida,"w") as salida:
  salida.write(union)
  salida.close()

archivo_lista = os.listdir(carpetaNombre)

for archivo_nombre in archivo_lista:
  archivo = open(carpetaNombre+archivo_nombre)
  texto = archivo.read()

  with open(carpetaNombre+archivo_nombre,"r") as archivo:
    lineas_lista = archivo.readlines()

  num_vacio=0
  num_lineas=0
  num_texto=0

  for linea in lineas_lista:
    if linea.strip() == "":
      num_vacio+=1
    else:
      num_texto+=1
    num_lineas+=1

  for simbolo in simbolos:
    texto = texto.replace(simbolo,"")

  palabras_lista = texto.split()

  print(archivo_nombre)

  if archivo_nombre == "documento.txt":
    palabra = input("Escribe la palabra a buscar en el documento: \n")
    res = False
    for linea in lineas_lista:
      if palabra in linea:
        res = True
        break
    if res == True:
      print("\nsi se encontro la palabra:",palabra,"\n")
    else:
      print("\nNo se encontro\n")

  print(sorted(palabras_lista))
  print("numero de palabras en el documento:", len(palabras_lista))
  print("Lineas totales:",num_lineas)
  print("Lineas con texto:",num_texto)
  print("Lineas vacias:",num_vacio)
  print("--------------------------------------")
  archivo.close()
