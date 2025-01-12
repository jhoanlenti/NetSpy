import requests
import time

def ip_public(intentos=1):
    url = "https://api.ipify.org"
    intentos_realizados = 0

    while intentos_realizados < intentos:
        try:
            response = requests.get(url)
            intentos_realizados += 1
            if response.status_code == 200:
                print(f"IP pública obtenida es: {response.text}")
                break
            else:
                print(f"Intento {intentos_realizados}: Error - Código de estado {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Intento {intentos_realizados}: Error de conexión: {e}")
        time.sleep(1)
