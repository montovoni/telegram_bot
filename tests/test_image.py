import requests

def generate_image(prompt):
    api_key = "sk-svcacct-7-jFpL_-d1PKQpZEad8JFsOg3kyGPHfRxK62pHpchV_WJG-H_ZGSF0weVqKR_gT3BlbkFJKeOvPZlaAv8_j8LSZduQdHGbccpNVPK55UBsbJE4coe-PheFCacWxbUSVo4A"
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

generate_image("um gato siamês branco")
