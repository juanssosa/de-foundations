import json
from decimal import Decimal

with open("data/empleados.json", encoding="utf-8") as archivo:
    empleados = json.load(archivo, parse_float=Decimal)
    totalNom = 0
for empleado in empleados:
    totalDev=0
    if empleado.get("conceptos") is None:
       print(f"El empleado {empleado['nombre']} no tiene concepto asociado")
    else:
       for concepto in empleado["conceptos"]:
          totalDev = totalDev + concepto["valor"]
       print(empleado["cedula"] + " " + empleado["nombre"] + " - Total devengado: " + f"{totalDev}")
       totalNom = totalNom + totalDev
print("Total nomina: "+f"{totalNom}")
