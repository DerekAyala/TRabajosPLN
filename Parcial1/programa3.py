archivo_nombre = "texto2.txt"

with open(archivo_nombre,"r") as archivo:
  lineas_lista = archivo.readlines()

palabra = input("Escribe la palabra a buscar en el documento: \n")
num_palabra=0
num_lineas=1
num_texto=0
num_vacio=0

for linea in lineas_lista:
  if linea.strip() == "":
    print("Linea",num_lineas,":","Esta linea esta vacia")
    num_lineas+=1
    num_vacio+=1
  else:
    print("Linea",num_lineas,":",linea)
    num_lineas+=1
    num_texto+=1
    if palabra in linea:
      num_palabra+=1
print("Lineas totales:",num_lineas)
print("Lineas con texto:",num_texto)
print("Lineas vacias:",num_vacio)
print("la palabra:",palabra,"se encuentra:",num_palabra,"veces en el documento")
