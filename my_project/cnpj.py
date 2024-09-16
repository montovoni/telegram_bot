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

def validar_cnpj(cnpj):
    # Remove qualquer caractere que não seja um dígito
    cnpj = ''.join(filter(str.isdigit, cnpj))

    # Verifica se o CNPJ tem exatamente 14 dígitos
    if len(cnpj) != 14:
        return False

    return True

def salvar_cnpj(cnpj_info, cnpj):
    file_name = f"consulta_cnpj_{cnpj}.txt"

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write("👤 DADOS CADASTRAIS\n\n")

        f.write(f"• CNPJ: {cnpj_info.get('cnpj', 'N/A')}\n")
        f.write(f"• NOME: {cnpj_info.get('nome', 'N/A')}\n")
        f.write(f"• FANTASIA: {cnpj_info.get('fantasia', 'N/A')}\n")
        f.write(f"• TIPO: {cnpj_info.get('tipo', 'N/A')}\n")
        f.write(f"• PORTE: {cnpj_info.get('porte', 'N/A')}\n")
        f.write(f"• NATUREZA JURÍDICA: {cnpj_info.get('natureza_juridica', 'N/A')}\n")
        f.write(f"• SITUAÇÃO: {cnpj_info.get('situacao', 'N/A')}\n")
        f.write(f"• DATA DA SITUAÇÃO: {cnpj_info.get('data_situacao', 'N/A')}\n")
        f.write(f"• ABERTURA: {cnpj_info.get('abertura', 'N/A')}\n")
        f.write(f"• ATIVIDADE PRINCIPAL: {cnpj_info.get('atividade_principal', [{'text': 'N/A'}])[0]['text']}\n")
        f.write(f"• ATIVIDADES SECUNDÁRIAS: {', '.join([a['text'] for a in cnpj_info.get('atividades_secundarias', [])])}\n")
        f.write(f"• CAPITAL SOCIAL: R$ {cnpj_info.get('capital_social', 'N/A')}\n")
        f.write(f"• TELEFONE: {cnpj_info.get('telefone', 'N/A')}\n")
        f.write(f"• EMAIL: {cnpj_info.get('email', 'N/A')}\n")
        f.write(f"• ENDEREÇO: {cnpj_info.get('logradouro', 'N/A')}, {cnpj_info.get('numero', 'N/A')} {cnpj_info.get('complemento', '')} - {cnpj_info.get('bairro', 'N/A')} - {cnpj_info.get('municipio', 'N/A')} - {cnpj_info.get('uf', 'N/A')}, {cnpj_info.get('cep', 'N/A')}\n\n")

        f.write(f"• SÓCIOS:\n")
        for socio in cnpj_info.get('qsa', []):
            f.write(f"  - {socio['nome']} ({socio['qual']})\n")
            if 'nome_rep_legal' in socio:
                f.write(f"    Representante Legal: {socio['nome_rep_legal']} ({socio['qual_rep_legal']})\n")

        f.write("\n")
        f.write(f"• SIMPLES NACIONAL: {'Sim' if cnpj_info.get('simples', {}).get('optante', False) else 'Não'}\n")
        f.write(f"  - Data de Opção: {cnpj_info.get('simples', {}).get('data_opcao', 'N/A')}\n")
        f.write(f"  - Data de Exclusão: {cnpj_info.get('simples', {}).get('data_exclusao', 'N/A')}\n\n")

        f.write(f"• MEI: {'Sim' if cnpj_info.get('simei', {}).get('optante', False) else 'Não'}\n")
        f.write(f"  - Data de Opção: {cnpj_info.get('simei', {}).get('data_opcao', 'N/A')}\n")
        f.write(f"  - Data de Exclusão: {cnpj_info.get('simei', {}).get('data_exclusao', 'N/A')}\n\n")

        f.write(f"• SITUAÇÃO ESPECIAL: {cnpj_info.get('situacao_especial', 'N/A')}\n")
        f.write(f"  - Data: {cnpj_info.get('data_situacao_especial', 'N/A')}\n")
        f.write(f"• STATUS: {cnpj_info.get('status', 'N/A')}\n\n")

        f.write(f"• ÚLTIMA ATUALIZAÇÃO: {cnpj_info.get('ultima_atualizacao', 'N/A')}\n")

    return file_name

# https://rapidapi.com/binfoconsultas/api/quadro-de-socios-cpf-cnpj/pricing
# https://www.sintegraws.com.br/api/documentacao-api-receita-federal.php
# https://developers.receitaws.com.br/#/operations/queryCNPJFree