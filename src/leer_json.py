import json
from decimal import Decimal


def leer_empleados(ruta):
    """Lee el archivo JSON y devuelve la lista de empleados."""
    with open("data/empleados.json", encoding="utf-8") as archivo:
       ruta = json.load(archivo, parse_float=Decimal)
    return ruta


def tiene_conceptos(empleado):
    """Devuelve True si el empleado trae la clave 'conceptos'; False si no."""
    if empleado.get("conceptos") is None:
       return False
    else:
       return True


def total_empleado(empleado):
    """Suma el valor de los conceptos de un empleado. Devuelve un Decimal."""
    totalDev=0
    for concepto in empleado["conceptos"]:
          totalDev += concepto["valor"]
    return Decimal(totalDev)


def main():
    empleados = leer_empleados("data/empleados.json")
    total_nomina = Decimal("0")
    for empleado in empleados:
        if tiene_conceptos(empleado) is False:
           print(f"El empleado {empleado['nombre']} no tiene concepto asociado")
        else:
           print(f"{empleado['cedula']} {empleado['nombre']} - Total devengado: {total_empleado(empleado)}")
           total_nomina += total_empleado(empleado)
    print(f"Total nomina: {total_nomina}")
if __name__ == "__main__":
    main()
