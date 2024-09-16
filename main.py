from telebot import TeleBot
import random, os
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from my_project.gemini import gerar_resposta_gemini, adicionar_mensagem
from my_project.cep import consultar_cep, salvar_cep
from my_project.cnpj import consultar_cnpj, salvar_cnpj
from my_project.advice import obter_conselho
from my_project.translator import traduzir_mensagem
from my_project.girlfriend import get_response_from_ai, get_voice_message
from dotenv import load_dotenv, find_dotenv

env_path = find_dotenv(os.path.join('..', 'my_project', '.env'))
load_dotenv(env_path)
auth_key = os.getenv("TELEGRAM_TOKEN")
bot = TeleBot(auth_key)

@bot.message_handler(commands=['start'])
def handle_first_message(message):
    chat_id = message.chat.id

    bot.send_message(chat_id,
        "🌟 <b>Bem-vindo ao Bot Interativo!</b> 🌟\n\n"
        "<b>Interaja com a inteligência artificial:</b>\n"
        "🔹 <b>/gemini</b> - <i>Digite sua mensagem para consultar o Gemini.</i>\n\n"
        "<b>Encontre informações rápidas:</b>\n"
        "🔹 <b>/cep</b> - <i>Informe o número do CEP para consulta.</i>\n"
        "🔹 <b>/cnpj</b> - <i>Informe o número do CNPJ para consulta.</i>\n\n"
      #  "🔹 <b>/cpf</b> - <i>Informe o CPF para consulta.</i>\n\n"
        "<b>Explore algumas outras opções</b>\n"
        "🔹 <b>/conselho</b> - <i>Receba um conselho inspirador para o seu dia.</i>\n"
        "🔹 <b>/links</b> - <i>Para quem gosta de viver perigosamente.</i>\n\n",
        parse_mode='HTML')

@bot.message_handler(commands=['gemini'])
def handle_custom_command(message):
    chat_id = message.chat.id
    user_message = message.text[len('/gemini '):].strip()

    if not user_message:
        bot.send_message(chat_id, "Por favor, envie uma mensagem após o comando /gemini.")
        return

    adicionar_mensagem(chat_id, user_message, role="user")
    loading_message = bot.send_message(chat_id, "Processando sua mensagem, aguarde...")

    try:
        answer = gerar_resposta_gemini(chat_id)
        answer = answer.replace('**', '')
        bot.send_message(chat_id, answer)

    except Exception as e:
        bot.send_message(chat_id, f"Erro ao processar a mensagem: {str(e)}")

    finally:
        bot.delete_message(chat_id, loading_message.message_id)

# Busca CEP
@bot.message_handler(commands=['cep'])
def handle_cep_command(message):
    chat_id = message.chat.id
    user_message_id = message.message_id
    cep = message.text[len('/cep '):].strip()

    if not cep:
        bot.send_message(chat_id, "Por favor, envie um número de CEP após o comando /cep.")
        return

    # Basic validation for CEP format (e.g., 8 digits)
    if not cep.isdigit() or len(cep) != 8:
        bot.send_message(chat_id, "CEP inválido. O CEP deve conter 8 dígitos numéricos.")
        return

    cep_info = consultar_cep(cep)
    if cep_info is None:
        bot.send_message(chat_id, "CEP inválido ou não encontrado.")
        return

    txt_file_name = salvar_cep(cep_info, cep)
    with open(txt_file_name, 'rb') as f_txt:
        bot.send_document(chat_id, f_txt, reply_to_message_id=user_message_id)

@bot.message_handler(commands=['conselho'])
def handle_advice_command(message):
    chat_id = message.chat.id

    slip_id = random.randint(1, 42)
    advice = obter_conselho(slip_id)
    advice_portuguese = traduzir_mensagem(advice)
    bot.send_message(chat_id, f"Conselho do dia: {advice_portuguese}")

# Busca CNPJ
@bot.message_handler(commands=['cnpj'])
def handle_cnpj_command(message):
    chat_id = message.chat.id
    user_message_id = message.message_id
    cnpj = message.text[len('/cnpj '):].strip()

    if not cnpj:
        bot.send_message(chat_id, "Por favor, envie um número de CNPJ após o comando /cnpj.")
        return

    try:
        cnpj_info = consultar_cnpj(cnpj)

        if cnpj_info is None:
            bot.send_message(chat_id, "O número do CNPJ não é válido. Verifique se o mesmo foi digitado corretamente..")
            return

        txt_file_name = salvar_cnpj(cnpj_info, cnpj)

        with open(txt_file_name, 'rb') as f_txt:
            # Adiciona o botão de exclusão
            delete_button = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🗑️ Excluir", callback_data=f"delete_{txt_file_name}")]]
            )
            bot.send_document(chat_id, f_txt, reply_markup=delete_button, reply_to_message_id=user_message_id)

    except Exception as e:
        bot.send_message(chat_id, f"Erro ao consultar o CNPJ: {str(e)}")

# Busca Links
@bot.message_handler(commands=['links'])
def handle_link_command(message):
    chat_id = message.chat.id

    response = (
        "🔹 <a href='https://t.me/VNMIDIAS'> Link 1: VNMIDIAS</a>\n"
        "🔹 <a href='https://t.me/onlyfansgratistiktok'> Link 2: OnlyFansTikTok</a>\n"
        "🔹 <a href='https://t.me/grupovip042923'> Link 3: GrupoVip</a>\n"
        "🔹 <a href='https://t.me/amador050923'> Link 4: Amador</a>\n"
    )

    bot.send_message(chat_id, response, parse_mode='HTML')

# simulador de namoro com IA
@bot.message_handler(commands=['namorada'])
def handle_namorada_command(message):
    chat_id = message.chat.id
    user_message = message.text[len('/namorada '):].strip()

    if not user_message:
        bot.send_message(chat_id, "Por favor, envie uma mensagem após o comando /namorada.")
        return

    ai_response = get_response_from_ai(user_message)
    audio_path = get_voice_message(ai_response)

    if audio_path:
        # Send the generated audio to the user
        with open(audio_path, 'rb') as audio_file:
            bot.send_audio(chat_id, audio_file)
        # Remove the temporary file after sending
        os.remove(audio_path)
    else:
        bot.send_message(chat_id, ai_response)

''' ===============================================================================================================- '''

# Função genérica para excluir arquivos
def excluir_arquivo(file_name, chat_id, user_id, message_id, user_message_id=None):
    try:
        # Verifica se o usuário tem permissão para excluir (solicitante original ou administrador)
        if user_is_admin(bot, chat_id, user_id):
            os.remove(file_name)
            confirmation_message = bot.send_message(chat_id, "Arquivo excluído com sucesso.")
        else:
            confirmation_message = bot.send_message(chat_id, "Você não tem permissão para excluir este arquivo.")

        # Exclui a mensagem original do Telegram (documento e mensagem do usuário)
        bot.delete_message(chat_id, message_id)
        if user_message_id:
            bot.delete_message(chat_id, user_message_id)

        # Exclui a mensagem de confirmação após alguns segundos
        bot.delete_message(chat_id, confirmation_message.message_id, timeout=5)

    except Exception as e:
        # Em caso de erro ao excluir o arquivo, envia a mensagem de erro e a remove após alguns segundos
        error_message = bot.send_message(chat_id, f"Erro ao excluir o arquivo: {str(e)}")
        bot.delete_message(chat_id, error_message.message_id, timeout=5)

# Função para lidar com os callbacks de botões
@bot.callback_query_handler(func=lambda call: call.data.startswith('delete_'))
def handle_delete_callback(call):
    file_name = call.data.split('_', 1)[1]
    user_id = call.from_user.id
    chat_id = call.message.chat.id

    # ID da mensagem que contém o documento
    message_id = call.message.message_id

    # Verifica se existe uma mensagem original do usuário para capturar seu ID
    user_message_id = call.message.reply_to_message.message_id if call.message.reply_to_message else None
    excluir_arquivo(file_name, chat_id, user_id, message_id, user_message_id)

# Função para verificar se o usuário é administrador
def user_is_admin(bot, chat_id, user_id):
    member = bot.get_chat_member(chat_id, user_id)
    return member.status in ['administrator', 'creator']

# Excluir o webhook existente (se houver)
bot.remove_webhook()

# Informe ao usuário que o bot está em execução
print("O bot está rodando! Pressione Ctrl + C para parar.")

# Inicie o bot
bot.polling()
