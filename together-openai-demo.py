# Load environment variables from the .env file
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['TOGETHER_API_KEY'] = os.getenv('TOGETHER_API_KEY')

from openai import OpenAI
client = OpenAI(
    api_key=os.getenv('TOGETHER_API_KEY'),
    base_url="https://api.together.xyz/v1" 
)

response = client.chat.completions.create(
  model="meta-llama/Llama-Vision-Free",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {
      "role": "user", 
      "content": "What are some fun things to do in New York?"
    }
  ]
)
print(response.choices[0].message.content)


