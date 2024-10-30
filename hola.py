import requests
 
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
    API_KEY = "AKIALALEMEL33243OLIA"  # Clave API
    datos = obtener_datos(API_KEY)
    print(datos)
 
if __name__ == "__main__":
    main()
