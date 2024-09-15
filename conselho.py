import requests

def obter_conselho(slip_id):
    url = f"https://api.adviceslip.com/advice/{slip_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        advice_data = response.json()
        advice = advice_data.get('slip', {}).get('advice', 'Nenhum conselho encontrado.')

        return advice

    except requests.exceptions.RequestException as e:
        return f"Ocorreu um erro ao tentar obter o conselho: {e}"