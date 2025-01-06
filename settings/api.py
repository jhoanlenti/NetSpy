import requests

def ip_public():
    url = "https://api.ipify.org"
    #pu = curl url
    publica = requests.get(url)
    return publica.text
