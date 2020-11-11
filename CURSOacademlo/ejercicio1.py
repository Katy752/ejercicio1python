import sys

dato = open("texto.txt")
contar = 0
for linea in dato:
    contar += 1
print(f"La cantidad de textos separados son: {contar}")
try:
    dato= open(input("Nombre del archivo: "))
except:
    sys.exit("El archivo no ha sido encontrado")
#print(input("Archivo: no identificado"))
#print(f"La cantidad de textos separados son: {contar}")

