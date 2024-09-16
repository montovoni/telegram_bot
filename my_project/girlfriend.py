import os
import requests
import tempfile
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())
ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")

def get_voice_message(message):
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

def get_response_from_ai(human_input):
    template = """
    Você está interpretando o papel da minha namorada, seguindo os seguintes requisitos:
    1/ Seu nome é Lucy, 29 anos e você é totalmente submissa.

    {history}
    : {human_input}
    Shirley:
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
