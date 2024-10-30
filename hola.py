import requests
import os
 
def obtener_datos(api_key):
    url = "https://api.kekw.com/datos"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    respuesta = requests.get(url, headers=headers)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return {"error": "No se pudieron obtener los datos"}
 
def main():
    api_key = os.environ.get('API_KEY')

if api_key:
    print("Clave API obtenida correctamente.")
else:
    print("No se encontró la clave API.")
 
if __name__ == "__main__":
    main()
