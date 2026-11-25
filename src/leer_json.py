import json
from decimal import Decimal
import sys


def leer_empleados(ruta):
    """Lee el archivo JSON y devuelve la lista de empleados."""
    ruta = sys.argv[1] if len(sys.argv) > 1 else "data/empleados.json"
    with open(ruta, encoding="utf-8") as archivo:
       emp = json.load(archivo, parse_float=Decimal)
    return emp


def tiene_conceptos(empleado):
    """Devuelve True si el empleado trae la clave 'conceptos'; False si no."""
    if empleado.get("conceptos") is None:
       return False
    else:
       return True


def total_empleado(empleado):
    """Suma el valor de los conceptos de un empleado. Devuelve un Decimal."""
    totalDev=Decimal(0)
    for concepto in empleado["conceptos"]:
          totalDev += concepto["valor"]
    return totalDev


def main():
    try:
       empleados = leer_empleados("data/empleados.json")
    except FileNotFoundError:
       print("El archivo no existe")
       sys.exit(1)
    except json.JSONDecodeError:
       print("El archivo existe, pero el JSON está mal formado")
       sys.exit(1)
    total_nomina = Decimal("0")
    for empleado in empleados:
        if not tiene_conceptos(empleado):
           print(f"El empleado {empleado['nombre']} no tiene concepto asociado")
        else:
           print(f"{empleado['cedula']} {empleado['nombre']} - Total devengado: {total_empleado(empleado)}")
           total_nomina += total_empleado(empleado)
    print(f"Total nomina: {total_nomina}")


if __name__ == "__main__":
    main()
