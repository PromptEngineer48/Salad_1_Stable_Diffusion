import requests
import base64
from PIL import Image
import io

import os

# load the environment variables
from dotenv import load_dotenv

load_dotenv()

# Replace 'your_salad_api_token' with your actual Salad API Token
salad_api_token = os.getenv("SALAD_API_TOKEN")
# The URL for the Salad API
url = os.getenv("SALAD_API_URL")

headers = {"Salad-Api-Key": salad_api_token, "Content-Type": "application/json"}

data = {
    "modelInputs": {
        "prompt": "A beautiful cat with long hair and a fluffy tail",
        "negative_prompt": "short hair, two heads, two tails",
        "num_inference_steps": 50,
        "guidance_scale": 7.5,
        "width": 512,
        "height": 512,
        "seed": 3239022079,
        "num_images_per_prompt": 2,
    },
    "callInputs": {
        "PIPELINE": "StableDiffusionPipeline",
        "SCHEDULER": "EulerAncestralDiscreteScheduler",
        "safety_checker": "true",
    },
}
# Send the request to the Salad API
response = requests.post(url, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    print("Success!")
    print("Response:")

    # Get the list of base64 encoded image data
    image_data_list = response.json()["images_base64"]

    # Loop through each image data and display it
    for i, image_data in enumerate(image_data_list):
        # Decode the Base64 encoded image data
        decoded_image_data = base64.b64decode(image_data)

        # Convert the decoded image data to bytes
        image_bytes = io.BytesIO(decoded_image_data)

        # Open the image using PIL
        image = Image.open(image_bytes)

        # Display the image
        image.show()

else:
    print("Error:", response.status_code, response.text)


# ***** Implementing the same code using matplotlib to display the images *****
# import base64
# import matplotlib.pyplot as plt

# if response.status_code == 200:
#     print("Success!")
#     print("Response:")

#     # Get the list of base64 encoded image data
#     image_data_list = response.json()["images_base64"]

#     # Loop through each image data and display it
#     for i, image_data in enumerate(image_data_list):
#         # Decode the Base64 encoded image data
#         decoded_image_data = base64.b64decode(image_data)

#         # Convert the decoded image data to bytes
#         image_bytes = io.BytesIO(decoded_image_data)

#         # Open the image using PIL
#         image = Image.open(image_bytes)

#         # Display the image using Matplotlib
#         plt.imshow(image)
#         plt.axis("off")  # Hide axis
#         plt.show()

# else:
#     print("Error:", response.status_code, response.text)
