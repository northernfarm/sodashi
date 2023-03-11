import os, sys
from dotenv import load_dotenv

from google.oauth2 import service_account

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))


class GoogleClient():
    def __init__(self):
        load_dotenv(".env")
        credentials = os.getenv("SODASHI_CREDENTIALS")
        self.credentials = service_account.Credentials.from_service_account_info(credentials)
        self.project_id = os.getenv("GOOGLE_PROJECT_ID")

    def get_storage_client(self):
        from google.cloud import storage
        return storage.Client(
            credentials=self.credentials,
            project=self.project_id
            )
    
    
    