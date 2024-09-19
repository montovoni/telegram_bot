from openai import OpenAI, RateLimitError, APIError, BadRequestError
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
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
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7
        )

        # Extrai a resposta do assistente
        resposta_texto = response.choices[0].message.content
        adicionar_mensagem_chatgpt(chat_id, resposta_texto, role="assistant")
        return resposta_texto

    except RateLimitError:
        raise Exception("Erro: Limite de taxa excedido. Por favor, verifique seu plano e detalhes de cobrança.")
    except BadRequestError as e:
        raise Exception(f"Erro de Requisição: {str(e)}")
    except APIError as e:
        raise Exception(f"Erro na API: {str(e)}")
    except Exception as e:
        raise Exception(f"Erro ao gerar resposta: {str(e)}")
