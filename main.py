import random, os
from telebot import TeleBot

from my_project.gemini import gerar_resposta_gemini, adicionar_mensagem_gemini
from my_project.chatgpt import gerar_resposta_chatgpt, adicionar_mensagem_chatgpt
from my_project.cep import consultar_viacep, salvar_viacep
from my_project.cnpj import consultar_informacoes_cnpj, salvar_cnpj, validar_cnpj
from my_project.advice import obter_conselho
from my_project.translator import traduzir_mensagem
from my_project.girlfriend import obter_resposta_lucy

from dotenv import load_dotenv, find_dotenv

env_path = find_dotenv(os.path.join('..', 'my_project', '.env'))
load_dotenv(env_path)
auth_key = os.getenv("TELEGRAM_TOKEN")
bot = TeleBot(auth_key)

# Dicionário para rastrear o estado de conversa de cada usuário
conversas_ativas = {}
historico_conversas = {}

@bot.message_handler(commands=['start'])
def iniciar_comando(message):
    chat_id = message.chat.id

    bot.send_message(chat_id,
        "🌟 <b>Bem-vindo ao Bot Interativo!</b> 🌟\n\n"
        "<b>Interaja com a inteligência artificial:</b>\n"
        "🔹 <b>/gemini</b> - <i>Digite sua mensagem para consultar o Gemini.</i>\n"
        "🔹 <b>/chatgpt</b> - <i>Digite sua mensagem para consultar o ChatGpt.</i>\n\n"
        "<b>Encontre informações rápidas:</b>\n"
        "🔹 <b>/cep</b> - <i>Informe o número do CEP para consulta.</i>\n"
        "🔹 <b>/cnpj</b> - <i>Informe o número do CNPJ para consulta.</i>\n\n"
      #  "🔹 <b>/cpf</b> - <i>Informe o CPF para consulta.</i>\n\n"
        "<b>Explore algumas outras opções</b>\n"
        "🔹 <b>/conselho</b> - <i>Receba um conselho inspirador para o seu dia.</i>\n"
        "🔹 <b>/links</b> - <i>Para quem gosta de viver perigosamente.</i>\n"
        "🔹 <b>/lucy</b> - <i>Converse com sua namorada virtual inteligente.</i>\n\n",
        parse_mode='HTML')

@bot.message_handler(commands=['gemini', 'gemini@montovoni', 'chatgpt', 'chatgpt@montovoni', 'lucy', 'lucy@montovoni'])
def iniciar_conversa(message):
    chat_id = message.chat.id
    comando = message.text.split()[0][1:].split('@')[0]

    conversas_ativas[chat_id] = comando
    bot.send_message(chat_id, f"Você está agora conversando com {comando.capitalize()}. Para parar, digite /sair.")

@bot.message_handler(commands=['sair', 'fechar'])
def encerrar_conversa(message):
    chat_id = message.chat.id
    if chat_id in conversas_ativas:
        del conversas_ativas[chat_id]
        bot.send_message(chat_id, "Conversa encerrada. Você pode começar uma nova conversa digitando um dos comandos (/gemini, /chatgpt, /lucy).")

@bot.message_handler(func=lambda message: message.chat.id in conversas_ativas)
def processar_mensagem(message):
    chat_id = message.chat.id
    comando = conversas_ativas.get(chat_id)

    if comando == 'gemini':
        consultar_gemini(message)
    elif comando == 'chatgpt':
        consultar_chatgpt(message)
    elif comando == 'lucy':
        relacionamento_virtual(message)

@bot.message_handler(commands=['chatgpt', 'chatgpt@montovoni'])
def consultar_chatgpt(message):
    chat_id = message.chat.id
    user_message = message.text.strip()

    adicionar_mensagem_chatgpt(chat_id, user_message, role="user")
    loading_message = bot.send_message(chat_id, "Processando sua mensagem, aguarde...")

    try:
        answer = gerar_resposta_chatgpt(chat_id)
        bot.send_message(chat_id, answer)

    except Exception as e:
        bot.send_message(chat_id, f"Erro ao processar a mensagem: {str(e)}")

    finally:
        bot.delete_message(chat_id, loading_message.message_id)

@bot.message_handler(commands=['gemini', 'gemini@montovoni'])
def consultar_gemini(message):
    chat_id = message.chat.id
    user_message = message.text.strip()

    adicionar_mensagem_gemini(chat_id, user_message, role="user")
    loading_message = bot.send_message(chat_id, "Processando sua mensagem, aguarde...")

    try:
        resposta = gerar_resposta_gemini(chat_id)
        resposta = resposta.replace('**', '')
        bot.send_message(chat_id, resposta)

    except Exception as e:
        bot.send_message(chat_id, f"Erro ao processar a mensagem: {str(e)}")

    finally:
        bot.delete_message(chat_id, loading_message.message_id)

@bot.message_handler(func=lambda message: message.text.lower().startswith('/cep'))
def consultar_cep(message):
    chat_id = message.chat.id
    user_message_id = message.message_id

    # Converte o texto do comando para minúsculas e remove espaços extras
    message_text = message.text.lower().strip()

    # Extrai o CEP, ignorando a variação de maiúsculas e minúsculas
    cep = message_text[len('/cep '):].strip()

    if not cep:
        bot.send_message(chat_id, "Por favor, envie um número de CEP após o comando /cep.")
        return

    # Validação básica para formato CEP (por exemplo, 8 dígitos)
    if not cep.isdigit() or len(cep) != 8:
        bot.send_message(chat_id, "CEP inválido. O CEP deve conter 8 dígitos numéricos.")
        return

    cep_info = consultar_viacep(cep)
    if cep_info is None:
        bot.send_message(chat_id, "CEP inválido ou não encontrado.")
        return

    # Pega o nome e o ID do usuário do Telegram
    usuario_nome = message.from_user.first_name + (f" {message.from_user.last_name}" if message.from_user.last_name else "")
    usuario_id = message.from_user.id

    txt_file_name = salvar_viacep(cep_info, cep, usuario_nome, usuario_id)
    with open(txt_file_name, 'rb') as f_txt:
        bot.send_document(chat_id, f_txt, reply_to_message_id=user_message_id)

@bot.message_handler(commands=['conselho'])
def consultar_conselho(message):
    chat_id = message.chat.id

    slip_id = random.randint(1, 42)
    advice = obter_conselho(slip_id)
    advice_portuguese = traduzir_mensagem(advice)
    bot.send_message(chat_id, f"Conselho do dia: {advice_portuguese}")

@bot.message_handler(func=lambda message: message.text.lower().startswith('/cnpj'))
def consultar_cnpj(message):
    chat_id = message.chat.id
    user_message_id = message.message_id

    # Converte o texto do comando para minúsculas e remove espaços extras
    message_text = message.text.lower().strip()

    # Extrai o CNPJ, ignorando a variação de maiúsculas e minúsculas
    cnpj = message_text[len('/cnpj '):].strip()

    # Valida o CNPJ antes de prosseguir
    if not validar_cnpj(cnpj):
        bot.send_message(chat_id, "O número do CNPJ não é válido ou não contém 14 dígitos. Verifique e tente novamente.")
        return

    try:
        cnpj_info = consultar_informacoes_cnpj(cnpj)

        if cnpj_info is None:
            bot.send_message(chat_id, "O número do CNPJ não é válido. Verifique se o mesmo foi digitado corretamente.")
            return

        # Pega o nome e o ID do usuário do Telegram
        usuario_nome = message.from_user.first_name + (f" {message.from_user.last_name}" if message.from_user.last_name else "")
        usuario_id = message.from_user.id

        txt_file_name = salvar_cnpj(cnpj_info, cnpj, usuario_nome, usuario_id)
        with open(txt_file_name, 'rb') as f_txt:
            bot.send_document(chat_id, f_txt, reply_to_message_id=user_message_id)

    except Exception as e:
        bot.send_message(chat_id, f"Erro ao consultar o CNPJ: {str(e)}")

@bot.message_handler(commands=['links'])
def consultar_links(message):
    chat_id = message.chat.id

    response = (
        "🔹 <a href='https://t.me/VNMIDIAS'> Link 1: VNMIDIAS</a>\n"
        "🔹 <a href='https://t.me/onlyfansgratistiktok'> Link 2: OnlyFansTikTok</a>\n"
        "🔹 <a href='https://t.me/grupovip042923'> Link 3: GrupoVip</a>\n"
        "🔹 <a href='https://t.me/amador050923'> Link 4: Amador</a>\n"
    )

    bot.send_message(chat_id, response, parse_mode='HTML')

@bot.message_handler(commands=['lucy', 'lucy@montovoni'])
def relacionamento_virtual(message):
    chat_id = message.chat.id
    user_message = message.text.strip()

    # Envia uma mensagem de carregamento para o usuário
    loading_message = bot.send_message(chat_id, "Processando sua mensagem, aguarde...")

    try:
        # Obtém o histórico existente ou inicia um novo se não houver
        if chat_id not in historico_conversas:
            historico_conversas[chat_id] = []

        # Gera a resposta da Lucy usando o histórico
        resposta_lucy = obter_resposta_lucy(historico_conversas[chat_id], user_message)

        # Adiciona a nova interação ao histórico
        historico_conversas[chat_id].append(f"Usuário: {user_message}")
        historico_conversas[chat_id].append(f"Lucy: {resposta_lucy}")

        bot.delete_message(chat_id, loading_message.message_id)
        bot.send_message(chat_id, resposta_lucy)

    except Exception as e:
        bot.delete_message(chat_id, loading_message.message_id)
        bot.send_message(chat_id, f"Ocorreu um erro ao processar sua mensagem: {str(e)}")

bot.remove_webhook()
print("O bot está rodando! Pressione Ctrl + C para parar.")
bot.polling()
