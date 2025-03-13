import requests

def consultar_cep(cep):
    """Camada de infraestrtura (Infrastructure Layer) conexão com serviços externos"""
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "erro" in data:
            return None
        return data
    return None