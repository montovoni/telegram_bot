import requests

def consultar_viacep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Check if the returned data contains an error
        if 'erro' in data:
            return None
        return data
    else:
        return None

def salvar_viacep(cep_info, cep):
    file_name = f"consulta_cep_{cep}.txt"

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write("# DADOS DO CEP\n\n")
        f.write(f"CEP: {cep_info.get('cep', 'N/A')}\n")
        f.write(f"LOGRADOURO: {cep_info.get('logradouro', 'N/A')}\n")
        f.write(f"COMPLEMENTO: {cep_info.get('complemento', 'N/A')}\n")
        f.write(f"BAIRRO: {cep_info.get('bairro', 'N/A')}\n")
        f.write(f"LOCALIDADE: {cep_info.get('localidade', 'N/A')}\n")
        f.write(f"UF: {cep_info.get('uf', 'N/A')}\n")
        f.write(f"IBGE: {cep_info.get('ibge', 'N/A')}\n")
        f.write(f"GIA: {cep_info.get('gia', 'N/A')}\n")
        f.write(f"DDD: {cep_info.get('ddd', 'N/A')}\n")
        f.write(f"SIAFI: {cep_info.get('siafi', 'N/A')}\n")

    return file_name