import requests

URL_COORDINADOR = "http://192.168.146.10:5000/procesar"

while True:
    frase = input("\nEscribe la frase del maestro (o 'salir'): ").strip()
    if frase.lower() == "salir":
        break

    resp = requests.post(URL_COORDINADOR, json={"frase": frase}, timeout=10)
    if resp.ok:
        datos = resp.json()
        print("Palabras volteadas:", datos["volteadas"])
        print("Frase original:    ", datos["original"])
    else:
        print("Error:", resp.text)