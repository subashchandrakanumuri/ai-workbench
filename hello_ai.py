import os
import sys
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, APIError

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY is not set in the environment variables.")
    print("Please set the OPENAI_API_KEY in your .env file or environment variables.")
    sys.exit(1)
client = OpenAI(api_key=api_key)
MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

# --the call--
try:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Be concise."},
            {"role": "user", "content": "What is generative ai in one sentence?"},
        ],
        temperature=0.7,
        max_tokens=100,
    )
    #response+error handling
    if response and response.choices:
        print("Response:", response.choices[0].message.content)
        print("Tokens used:", response.usage.total_tokens)
    else:
        print("No response received from the API.")
except AuthenticationError as auth_err:
    print("Authentication Error:", auth_err)
    print("Please check your OPENAI_API_KEY.")
except APIConnectionError as conn_err:
    print("Connection Error:", conn_err)
    print("Please check your internet connection.")
except Exception as e:
    print("An error occurred:", traceback.format_exc())