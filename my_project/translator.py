import deepl
import os
from dotenv import load_dotenv, find_dotenv

# Carregar variáveis de ambiente
load_dotenv(find_dotenv())
auth_key = os.getenv("DEEPL_API")

# Inicializa o tradutor com a chave de autenticação
translator = deepl.Translator(auth_key)

def traduzir_mensagem(mensagem):
    # Traduz o texto da mensagem para português
    return translator.translate_text(mensagem, target_lang="PT-BR")

# - https://developers.deepl.com/docs/v/pt-br