import requests
import os
import dotenv


dotenv.load_dotenv(dotenv_path="src/variables.env")
print(os.getenv("PRIVATE_KEY"))