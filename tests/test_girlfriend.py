'''
@bot.message_handler(commands=['lucy', 'lucy@montovoni'])
def relacionamento_virtual(message):
    chat_id = message.chat.id
    user_message = message.text.strip()

    # Envia uma mensagem de carregamento para o usuário
    loading_message = bot.send_message(chat_id, "Processando sua mensagem, aguarde...")

    try:
        resposta_lucy = obter_resposta_lucy(user_message)

        # Gera um identificador único para a resposta
        resposta_id = str(uuid.uuid4())
        respostas_armazenadas[resposta_id] = resposta_lucy

        # Cria um markup com botão para ouvir o áudio
        markup = InlineKeyboardMarkup()
        botao_escutar = InlineKeyboardButton("🎧 Ouvir em Áudio", callback_data=f"ouvir_audio:{resposta_id}")
        markup.add(botao_escutar)

        bot.delete_message(chat_id, loading_message.message_id)
        bot.send_message(chat_id, resposta_lucy)  # , reply_markup=markup)

    except Exception as e:
        bot.delete_message(chat_id, loading_message.message_id)
        bot.send_message(chat_id, f"Ocorreu um erro ao processar sua mensagem: {str(e)}")


# Callback para quando o usuário clica no botão "Ouvir em Áudio"
@bot.callback_query_handler(func=lambda call: call.data.startswith("ouvir_audio:"))
def enviar_audio(call):
    chat_id = call.message.chat.id
    resposta_id = call.data.split(":", 1)[1]  # Extrai o ID da resposta

    # Recupera a resposta da Lucy usando o identificador
    resposta_lucy = respostas_armazenadas.get(resposta_id, None)

    if resposta_lucy:
        # Gera o áudio da resposta usando a função obter_voz
        audio_lucy = obter_voz(resposta_lucy)

        if audio_lucy:
            # Envia o áudio como mensagem de voz e guarda a mensagem
            with open(audio_lucy, 'rb') as audio_file:
                sent_message = bot.send_voice(chat_id, audio_file)

            # Espera um tempo curto antes de deletar o áudio
            time.sleep(5)  # tempo ajustável para permitir a reprodução
            bot.delete_message(chat_id, sent_message.message_id)

            # Remove o arquivo temporário
            os.remove(audio_lucy)
        else:
            bot.send_message(chat_id, "Não foi possível gerar o áudio.")
    else:
        bot.send_message(chat_id, "Resposta não encontrada ou expirada.")
'''