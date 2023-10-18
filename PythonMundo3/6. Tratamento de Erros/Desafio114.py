import requests

def verifica_site(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "O site está acessível"
        else:
            return "O site não está acessível"
    except requests.ConnectionError:
        return "O site não está acessível"

print(verifica_site("http://www.pudim.com.br"))
