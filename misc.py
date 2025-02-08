import requests
import base64
import json
from PIL import Image
import io

url = "https://2f27-69-55-141-168.ngrok-free.app/analyze-waste/"
data = {
    "image_url": "https://storage.googleapis.com/centralhack-postmen/projects/1739006427026-image.jpg"
}

response = requests.post(url, json=data)
response_data = response.json()

# Get the base64 image data
b64_image = response_data['visualization']

# Decode base64 string to bytes
image_bytes = base64.b64decode(b64_image)

# Create image from bytes
image = Image.open(io.BytesIO(image_bytes))

# Save the image
output_path = 'waste_analysis_visualization.png'
image.save(output_path)
print(f"Image saved to {output_path}")

# Print the analytics data
print("\nAnalytics:")
print(json.dumps(response_data['analytics'], indent=2))