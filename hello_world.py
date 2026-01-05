import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
debug_mode = os.getenv("DEBUG")
name = os.getenv("MY_NAME")

print (f"[ENV TEST] Hello, {name}")
print (f"[ENV TEST] API key: {api_key}")
print (f"[ENV TEST] Debug_mode: {debug_mode}")

#FINISH

#saab