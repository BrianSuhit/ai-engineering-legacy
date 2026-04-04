import os
from google import genai
from dotenv import load_dotenv
from PIL import Image

# Load environment variables and initialize the AI client
load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the path for the image to be analyzed
image_path = "wall-e.jpg"

# Try to open and load the image, with error handling
try:
    img = Image.open(image_path)
    print(f"✅ Image '{image_path}' loaded successfully.")
    print(f"Dimensions: {img.size}")
except Exception as e:
    print(f"❌ Error opening the image: {e}")
    exit()
    
# Prepare the multimodal prompt with the image and text instructions
instructions = [
    img, 
    "Analyze this image in detail. Identify any objects or people, the predominant colors, and describe the context of the scene."
]

print("🧠 Gemini is looking at and analyzing the image...")

# Send the request to the Gemini model
response = client.models.generate_content(
    model="gemini-3-flash-preview", 
    contents=instructions
)

# Print the analysis received from the AI
print("\n" + "="*40)
print("🤖 AI VISUAL ANALYSIS:")
print("="*40)
print(response.text)