import deepl

# Substitua pela sua chave
auth_key = "API"

# Inicializa o tradutor com a chave de autenticação
translator = deepl.Translator(auth_key)

def traduzir_mensagem(mensagem):
    # Traduz o texto da mensagem para português
    return translator.translate_text(mensagem, target_lang="PT-BR")

'''
mensagem = 'Hello world'
mensagem_traduzida = traduzir_mensagem(mensagem)  # Traduz a mensagem
print(mensagem_traduzida)  # Imprime a mensagem traduzida
'''