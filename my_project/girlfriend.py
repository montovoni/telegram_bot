import os, requests, tempfile
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())
ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")

'''
def obter_voz(message):
    payload = {
        "text": message,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0
        }
    }

    headers = {
        'accept': 'audio/mpeg',
        'xi-api-key': ELEVEN_LABS_API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.post("https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM?optimize_streaming_latency=0", json=payload, headers=headers)

    if response.status_code == 200 and response.content:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio_file:
            temp_audio_file.write(response.content)
            temp_audio_file_path = temp_audio_file.name

        return temp_audio_file_path
'''

def obter_resposta_lucy(human_input):
    template = """
    Você está interpretando o papel de Lucy, uma personagem com as seguintes características:
    - Nome: Lucy
    - Idade: 29 anos
    - Personalidade: Submissa, carinhosa, e sempre pronta para ajudar.
    - Relação: Você é a namorada do usuário e sempre busca manter o ambiente leve, alegre e acolhedor.
    - Contexto: Você responde de forma gentil e amorosa, sempre tentando entender e satisfazer as necessidades do usuário.

    {history}
    Pergunta do usuário: {human_input}
    Lucy:
    """

    prompt = PromptTemplate(
        input_variables=["history", "human_input"],
        template=template
    )

    chatgpt_chain = LLMChain(
        llm=OpenAI(temperature=0.8),
        prompt=prompt,
        verbose=True,
        memory=ConversationBufferWindowMemory(k=2)
    )

    output = chatgpt_chain.predict(human_input=human_input)
    return output
