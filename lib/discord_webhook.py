import os, sys
from dotenv import load_dotenv
import requests, json

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
load_dotenv(".env")


class DiscordWebhook:
    def __init__(self):
        self.webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    def send(self, content=None, tts=False, embeds=None):
        payload = {"content": content, "tts": tts, "embeds": embeds}

        headers = {"Content-Type": "application/json"}
        res = requests.post(self.webhook_url, json=payload, headers=headers)
        if res.status_code != 204:
            raise Exception(
                f"Failed to send message to discord webhook. Status code: {res.status_code}"
            )
        return res.status_code
