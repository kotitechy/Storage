from huggingface_hub import HfApi

# Initialize the API
api = HfApi()

try:
    # Login to Hugging Face
    api.login(email="kummariyeshwanth9@gmail.com", password="yeshwanthkummari197")

    # Generate a new API key
    api_key = api.create_api_key()
    print(f"Your new API key: {api_key}")

except Exception as e:
    print(f"An error occurred: {e}")
