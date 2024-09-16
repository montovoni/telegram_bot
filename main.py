from telebot import TeleBot
import random, os

from my_project.gemini import gerar_resposta_gemini, adicionar_mensagem_gemini
from my_project.chatgpt import gerar_resposta_chatgpt, adicionar_mensagem_chatgpt

from my_project.cep import consultar_viacep, salvar_viacep
from my_project.cnpj import consultar_informacoes_cnpj, salvar_cnpj, validar_cnpj

from my_project.advice import obter_conselho
from my_project.translator import traduzir_mensagem

from my_project.girlfriend import obter_resposta_lucy #, obter_voz

from dotenv import load_dotenv, find_dotenv

env_path = find_dotenv(os.path.join('..', 'my_project', '.env'))
load_dotenv(env_path)
auth_key = os.getenv("TELEGRAM_TOKEN")
bot = TeleBot(auth_key)

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

@bot.message_handler(commands=['chatgpt'])
def consultar_chatgpt(message):
    chat_id = message.chat.id
    user_message = message.text[len('/chatgpt '):].strip()

    # Verifica se a mensagem do usuário não está vazia
    if not user_message:
        bot.send_message(chat_id, "Por favor, envie uma mensagem após o comando /chatgpt.")
        return

    adicionar_mensagem_chatgpt(chat_id, user_message, role="user")
    loading_message = bot.send_message(chat_id, "Processando sua mensagem, aguarde...")

    try:
        # Obtém a resposta do OpenAI
        answer = gerar_resposta_chatgpt(chat_id)
        bot.send_message(chat_id, answer)

    except Exception as e:
        bot.send_message(chat_id, f"Erro ao processar a mensagem: {str(e)}")

    finally:
        bot.delete_message(chat_id, loading_message.message_id)

@bot.message_handler(commands=['gemini'])
def consultar_gemini(message):
    chat_id = message.chat.id
    user_message = message.text[len('/gemini '):].strip()

    if not user_message:
        bot.send_message(chat_id, "Por favor, envie uma mensagem após o comando /gemini.")
        return

    adicionar_mensagem_gemini(chat_id, user_message, role="user")
    loading_message = bot.send_message(chat_id, "Processando sua mensagem, aguarde...")

    try:
        answer = gerar_resposta_gemini(chat_id)
        answer = answer.replace('**', '')
        bot.send_message(chat_id, answer)

    except Exception as e:
        bot.send_message(chat_id, f"Erro ao processar a mensagem: {str(e)}")

    finally:
        bot.delete_message(chat_id, loading_message.message_id)

@bot.message_handler(commands=['cep'])
def consultar_cep(message):
    chat_id = message.chat.id
    user_message_id = message.message_id
    cep = message.text[len('/cep '):].strip()

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

    txt_file_name = salvar_viacep(cep_info, cep)
    with open(txt_file_name, 'rb') as f_txt:
        bot.send_document(chat_id, f_txt, reply_to_message_id=user_message_id)

@bot.message_handler(commands=['conselho'])
def consultar_conselho(message):
    chat_id = message.chat.id

    slip_id = random.randint(1, 42)
    advice = obter_conselho(slip_id)
    advice_portuguese = traduzir_mensagem(advice)
    bot.send_message(chat_id, f"Conselho do dia: {advice_portuguese}")

@bot.message_handler(commands=['cnpj'])
def consultar_cnpj(message):
    chat_id = message.chat.id
    user_message_id = message.message_id
    cnpj = message.text[len('/cnpj '):].strip()

    # Valida o CNPJ antes de prosseguir
    if not validar_cnpj(cnpj):
        bot.send_message(chat_id, "O número do CNPJ não é válido ou não contém 14 dígitos. Verifique e tente novamente.")
        return

    try:
        cnpj_info = consultar_informacoes_cnpj(cnpj)  # Updated function call

        if cnpj_info is None:
            bot.send_message(chat_id, "O número do CNPJ não é válido. Verifique se o mesmo foi digitado corretamente.")
            return

        txt_file_name = salvar_cnpj(cnpj_info, cnpj)

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

@bot.message_handler(commands=['lucy'])
def relacionamento_virtual(message):
    chat_id = message.chat.id
    user_message = message.text[len('/lucy '):].strip()

    if not user_message:
        bot.send_message(chat_id, "Por favor, envie uma mensagem após o comando /lucy.")
        return

    resposta_lucy = obter_resposta_lucy(user_message)

    # Apenas enviando a mensagem de texto
    bot.send_message(chat_id, resposta_lucy)

    '''
    Se desejar manter o código de áudio para uso futuro, você pode descomenta-lo:
    audio_lucy = obter_voz(resposta_lucy)

    if audio_lucy:
        # Enviar o áudio gerado para o usuário
        with open(audio_lucy, 'rb') as audio_file:
            bot.send_audio(chat_id, audio_file)
        # Remove the temporary file after sending
        os.remove(audio_lucy)
    else:
        bot.send_message(chat_id, resposta_lucy)
    '''

# ==================================================================================================================== #

bot.remove_webhook()
print("O bot está rodando! Pressione Ctrl + C para parar.")
bot.polling()
