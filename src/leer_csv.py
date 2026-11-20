import csv

with open("data/empleados.csv", encoding="utf-8", newline="") as archivo:
    lector = csv.DictReader(archivo, delimiter=";")
    total=0
    i=0
    for fila in lector:
        total = total + int(fila["salario"])
        i=i+1
        print(fila)
        print(type(fila["salario"]))


print(f"Total nomina: {total}")
if i != 0:
	print(f"Salario promedio: {int(total/i)}")
	print(f"Salario promedio: {total/i}")
	print(f"Salario promedio: round(total/i)")
else:
	print("No se puede dividir entre 0")
