import requests

def consultar_cnpj(cnpj):
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj": cnpj, "plugin": "RF"}
    response = requests.get(url, params=querystring)

    if response.status_code == 200:
        data = response.json()
        if data.get('status') == 'ERROR':
            return None
        return data
    else:
        return None

consulta = consultar_cnpj('06006848000104')
print(consulta)

# https://rapidapi.com/binfoconsultas/api/quadro-de-socios-cpf-cnpj/pricing
# https://www.sintegraws.com.br/api/documentacao-api-receita-federal.php
# https://developers.receitaws.com.br/#/operations/queryCNPJFree