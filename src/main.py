import requests
import os
import dotenv
import webbrowser
from urllib.parse import urlencode


dotenv.load_dotenv(dotenv_path="src/variables.env")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

auth_headers = {"response_type" : "code",
                "client_id" : CLIENT_ID,
                "redirect_uri": "http://localhost:8080/callback",
                "scope" : "playlist-read-private"}

webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

"""response = requests.post(url="https://accounts.spotify.com/api/token",
              headers={"Content-Type" : "application/x-www-form-urlencoded"},
              data= {"grant_type" : "client_credentials",
                     "client_id" : CLIENT_ID,
                     "client_secret" : CLIENT_SECRET}) if "response" not in locals() else None

access_token = response.json()["access_token"]
print(access_token)"""