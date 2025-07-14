import requests
import os
import uuid

url = "https://api.a4f.co/v1/images/generations"
headers = {
    "Authorization": 'Bearer A4F-api-key',  # Replace with your actual API key
    "Content-Type": "application/json"
}
data = {
    "model": "provider-4/imagen-3",
    "prompt": "car in the clouds",# put your prompt here
    "n": 1,
    "size": "1024x1024"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print("Image generation successful:")
    print(result)
    
    image_url = result['data'][0]['url']  
    
    # Download and save the image
    image_response = requests.get(image_url)
    filename = f"generated_image_{uuid.uuid4().hex[:8]}.png"
    filepath = os.path.join("images", filename)
    
    with open(filepath, 'wb') as f:
        f.write(image_response.content)
    
    print(f"Image downloaded to: {filepath}")
    
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)