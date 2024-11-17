# Load environment variables from the .env file
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['TOGETHER_API_KEY'] = os.getenv('TOGETHER_API_KEY')

from together import Together

client = Together(api_key=os.getenv('TOGETHER_API_KEY'))

response = client.chat.completions.create(
    model="meta-llama/Llama-Vision-Free",
    messages=[
        {"role": "user", 
         "content": "What are some fun things to do in New York?"
        }
    ]
)
print(response.choices[0].message.content)