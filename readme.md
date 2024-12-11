# Bot de Telegram com Integrações de API

Este projeto é um bot de Telegram que integra diversas APIs, como a API do Google Generative AI e a API de tradução DeepL, para oferecer funcionalidades avançadas de conversação e tradução diretamente no Telegram.

## Requisitos
- Python 3.7 ou superior
  
## Instalação

Siga os passos abaixo para configurar o bot na sua máquina local:

1. **Clone este repositório**:

   ```bash
   git clone https://github.com/seu-usuario/telegram-bot.git
   cd telegram-bot
   ```
   
2. **Instale as dependências necessárias:**

   Abra o terminal ou prompt de comando e execute os seguintes comandos:

   ```bash
   pip install telebot
   pip install --upgrade pip
   pip install google-generativeai
   pip install deepl

   pip install openai
   pip install python-dotenv
   pip install langchain
   pip install langchain_community
   pip install langchain-openai
   ```

   - `pip install telebot`: Instala a biblioteca `telebot`, utilizada para criar bots no Telegram.
   - `pip install --upgrade pip`: Atualiza o `pip` (gerenciador de pacotes do Python) para a versão mais recente.
   - `pip install google-generativeai`: Instala a biblioteca `google-generativeai`, que permite interagir com a API Generative AI do Google.
   - `pip install deepl`: Instala a biblioteca `deepl`, que permite a integração com a API de tradução do DeepL.
   - `pip install openai`: Instala a biblioteca oficial da `OpenAI`, usada para interagir com as APIs da OpenAI, como GPT-3 e GPT-4.
   - `pip install python-dotenv:` Instala a biblioteca `python-dotenv`, que facilita o gerenciamento de variáveis de ambiente a partir de um arquivo .env.
   - `pip install langchain`: Instala a biblioteca `langchain`, que ajuda a construir aplicativos com grandes modelos de linguagem.
   - `pip install langchain_community`: Instala a biblioteca `langchain_community`, uma extensão da langchain com contribuições da comunidade para funcionalidades adicionais. 

## Obtenha o Token de API do Telegram

Para usar o bot do Telegram, você precisa obter um token de API. Siga os passos abaixo:

1. **Abra o Telegram e procure por "BotFather" na barra de pesquisa. O BotFather é o bot oficial do Telegram para criação e gerenciamento de bots.**

2. **Inicie uma conversa com o BotFather clicando no nome dele e depois em "Start".**

3. **Crie um novo bot enviando o comando /newbot para o BotFather.**

4. **Siga as instruções do BotFather:**

   - Escolha um nome para o seu bot (ex: MeuBotLegal).
   - Escolha um nome de usuário para o seu bot que termine com "bot" (ex: meubot_legal_bot).
     
5. **Receba o Token de API: Depois de criar o bot, o BotFather enviará uma mensagem com o token de API do seu bot. Esse token será uma sequência de caracteres como 123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ.**

5. **Guarde este token com segurança: Você precisará dele para configurar seu bot no arquivo .env do projeto.**

## Configuração

1. **Obtenha suas chaves de API:**

   - Acesse o [Google Cloud Console](https://console.cloud.google.com/) para obter a chave de API do Google Generative AI.
   - Acesse o [DeepL Pro](https://www.deepl.com/pro-api) para obter a chave de API do DeepL.
   - Acesse o [ChatGpt](https://platform.openai.com/api-keys) para obter a chave de API do ChatGpt.
   - Acesse o [ElevenLabs](https://elevenlabs.io/) para obter a chave de API do ElevenLabs.

2. **Configure as chaves de API:**

   Crie um arquivo `.env` na raiz (\telegram_bot\my_project) do projeto e adicione suas chaves de API:

   ```plaintext
   OPENAI_API_KEY=your_apy_chatgpt
   ELEVEN_LABS_API_KEY=your_apy_elevenlabs
   TELEGRAM_TOKEN=your_telegram_api_key
   GOOGLE_GENERATIVE_API_KEY=your_google_api_key
   DEEPL_API=your_deepl_api_key
   ```

## Executando o Bot

Para executar o bot, certifique-se de que você está no diretório raiz do projeto e execute:

```bash
python main.py
```

Certifique-se de que o terminal está na pasta correta onde o arquivo `main.py` do bot está localizado.

## Uso

Após iniciar o bot, você pode utilizar os seguintes comandos no Telegram:

- `/start` - Inicia o bot e exibe uma mensagem de boas-vindas.
  
- `/gemini` - Digite sua mensagem para consultar o Gemini.
- `/chatgpt` - Digite sua mensagem para consultar o ChatGPT.
- `/cep` - Informe o número do CEP para consulta.
- `/cnpj` - Informe o número do CNPJ para consulta.
- `/conselho` - Receba um conselho inspirador para o seu dia.
- `/links` - Para quem gosta de viver perigosamente (detalhar se necessário).
- `/lucy` - Converse com sua namorada virtual inteligente.

## Contribuindo

Sinta-se à vontade para contribuir com este projeto. Para isso:

1. Faça um fork do projeto.
2. Crie uma branch para a sua feature: `git checkout -b minha-feature`.
3. Faça commit das suas alterações: `git commit -m 'Minha nova feature'`.
4. Envie para o branch: `git push origin minha-feature`.
5. Abra um pull request.

## Licença



Este projeto está licenciado sob a [https://github.com/montovoni]

## Contato

Para mais informações ou sugestões, entre em contato através do [montovoni@hotmail.com](mailto:montovoni@hotmail.com).


