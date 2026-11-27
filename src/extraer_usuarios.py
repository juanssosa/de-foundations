import requests
import json
import sys

TIMEOUT_SEGUNDOS = 10
URL_POR_DEFECTO = "https://jsonplaceholder.typicode.com/users"
RUTA = "/home/juanssosa/proyectos/de-foundations/data/raw/usuarios.json"

#obtener_usuarios(url, timeout): hace el GET, llama a raise_for_status() y devuelve el .json(). Sin try y sin print (ya sabes por qué).
def obtener_usuarios(url, timeout):
   respuesta = requests.get(
    url,
    params={"_limit": 5},        # parámetros de la URL: ?_limit=5
    timeout=timeout,                  # segundos máximos de espera
   )
   respuesta.status_code            # 200
   respuesta.raise_for_status()     # lanza HTTPError si es 4xx o 5xx; si no, no hace nada
   datos = respuesta.json()
   return datos

#guardar_json(datos, ruta): escribe los datos en un archivo con json.dump(datos, archivo, ensure_ascii=False, indent=2). Investiga qué hace cada uno de los dos parámetros.
def guardar_json(datos, ruta):
   with open(ruta, "w", encoding="utf-8") as d:
      json.dump(datos, d, ensure_ascii=False, indent=2)

#main(): llama a las dos funciones y captura las tres excepciones de la tabla. Cada una escribe su mensaje en stderr y termina con sys.exit(1). Guarda el resultado en data/raw/usuarios.json.
def main():
   url = sys.argv[1] if len(sys.argv) > 1 else URL_POR_DEFECTO
   try:
      datos = obtener_usuarios(url, TIMEOUT_SEGUNDOS)
      guardar_json(datos, RUTA)
   except requests.exceptions.Timeout:
      print(f"ERROR: la API no respondió en {TIMEOUT_SEGUNDOS} segundos: {url}", file=sys.stderr)
      sys.exit(1)
   except requests.exceptions.ConnectionError as e:
      print(f"ERROR: no se pudo conectar a {url}: {e}", file=sys.stderr)
      sys.exit(1)
   except requests.exceptions.HTTPError as e:
      print(f"ERROR: la API respondió con un error HTTP: {e}", file=sys.stderr)
      sys.exit(1)

if __name__ == "__main__":
   main()
