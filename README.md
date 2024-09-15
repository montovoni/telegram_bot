
# Bot de Telegram com Integrações de API

Este projeto é um bot de Telegram que integra diversas APIs, como a API do Google Generative AI e a API de tradução DeepL, para oferecer funcionalidades avançadas de conversação e tradução diretamente no Telegram.

## Requisitos

- Python 3.7 ou superior
- Conta e chave de API para o [Google Generative AI](https://developers.google.com/).
- Conta e chave de API para o [DeepL](https://www.deepl.com/pro-api).

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
   ```

   - `pip install telebot`: Instala a biblioteca `telebot`, utilizada para criar bots no Telegram.
   - `pip install --upgrade pip`: Atualiza o `pip` (gerenciador de pacotes do Python) para a versão mais recente.
   - `pip install google-generativeai`: Instala a biblioteca `google-generativeai`, que permite interagir com a API Generative AI do Google.
   - `pip install deepl`: Instala a biblioteca `deepl`, que permite a integração com a API de tradução do DeepL.

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

2. **Configure as chaves de API:**

   Crie um arquivo `.env` na raiz do projeto e adicione suas chaves de API:

   ```plaintext
   TELEGRAM_API_KEY=your_telegram_api_key
   GOOGLE_GENERATIVE_API_KEY=your_google_api_key
   DEEPL_API_KEY=your_deepl_api_key
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
- `/mensagem` - Envia uma mensagem usando a API do Google Generative AI.
- `/traduzir` - Traduz um texto para o idioma desejado utilizando a API do DeepL.
- `/help` - Lista todos os comandos disponíveis e como usá-los.

## Contribuindo

Sinta-se à vontade para contribuir com este projeto. Para isso:

1. Faça um fork do projeto.
2. Crie uma branch para a sua feature: `git checkout -b minha-feature`.
3. Faça commit das suas alterações: `git commit -m 'Minha nova feature'`.
4. Envie para o branch: `git push origin minha-feature`.
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a [https://github.com/montovoni](LICENSE).

## Contato

Para mais informações ou sugestões, entre em contato através do [montovoni@hotmail.com](mailto:montovoni@hotmail.com).
