import openai,os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

# Dicionário para armazenar o histórico de conversas
chat_histories = {}

def adicionar_mensagem_chatgpt(chat_id, mensagem, role="user"):
    # Adiciona a mensagem ao histórico de conversas
    if chat_id not in chat_histories:
        chat_histories[chat_id] = []

    chat_histories[chat_id].append({"role": role, "content": mensagem})

def gerar_resposta_chatgpt(chat_id):
    # Constrói o histórico da conversa para enviar ao OpenAI
    messages = [{"role": entry["role"], "content": entry["content"]} for entry in chat_histories[chat_id]]

    try:
        # Solicitação para o OpenAI GPT
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Utilize o modelo desejado
            messages=messages,
            temperature=0.7
        )

        # Extrai a resposta do assistente
        resposta_texto = response['choices'][0]['message']['content']
        adicionar_mensagem_chatgpt(chat_id, resposta_texto, role="assistant")
        return resposta_texto

    except openai.error.RateLimitError:
        raise Exception("Erro: Limite de taxa excedido. Por favor, verifique seu plano e detalhes de cobrança.")
    except openai.error.OpenAIError as e:
        raise Exception(f"Erro ao gerar resposta: {str(e)}")
