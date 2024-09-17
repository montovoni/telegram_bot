import google.generativeai as genai

genai.configure(api_key="AIzaSyCTGDxzEQEsdoOKs2ZpXmrK4aofv-gOO3Q")
model = genai.GenerativeModel('gemini-1.5-flash')

chat_histories = {}

def adicionar_mensagem_gemini(chat_id, mensagem, role="user"):

    if chat_id not in chat_histories:
        chat_histories[chat_id] = []

    chat_histories[chat_id].append({"role": role, "content": mensagem})

def gerar_resposta_gemini(chat_id):

    conversation_history = "\n".join(
        f"{item['role']}: {item['content']}" if isinstance(item, dict) else item
        for item in chat_histories[chat_id]
    )

    try:
        response = model.generate_content(contents=[conversation_history], stream=True)
        response.resolve()
        resposta_texto = response.text
        adicionar_mensagem_gemini(chat_id, resposta_texto, role="Gemini")
        return resposta_texto

    except Exception as e:
        raise Exception(f"Erro ao gerar resposta: {str(e)}")
