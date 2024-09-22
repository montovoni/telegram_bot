import requests, os
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())


def generate_image(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    url = "https://api.openai.com/v1/images/generations"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "dall-e-3",
        "prompt": prompt,
        "num_images": 1,
        "size": "1024x1024"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Check for HTTP errors

        image_url = response.json()['data'][0]['url']
        print(f"URL da imagem gerada: {image_url}")
        return image_url

    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro: {e}")
