import openai

def gerar_resposta_chatgpt(user_message):
    api_key = "SUA_API"

    openai.api_key = api_key

    try:
        # Solicitação para o OpenAI GPT
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Utilize o modelo desejado
            messages=[{"role": "user", "content": user_message}],
            temperature=0.7
        )

        # Retorna a resposta do assistente
        return response['choices'][0]['message']['content']

    except openai.error.RateLimitError:
        return "Erro: Limite de taxa excedido. Por favor, verifique seu plano e detalhes de cobrança."
    except openai.error.OpenAIError as e:
        return f"Erro: {str(e)}"

# Teste da função
resposta = gerar_resposta_chatgpt("qual é a raiz quadrada de 140000000000000?")
print(resposta)

