import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/spreadsheets']

SPREADSHEET_ID = "1h3bTaLiAv0k3eOTKVYHXGoQ7FBn98-jryhJ83N0jhds"

def googleSheetsWriter(infoList: list):
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("clientcredentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())
     
    try:
        service = build("sheets", "v4", credentials = credentials)
        sheet = service.spreadsheets()

        """
        rows = [
        ["Hello World", "שלום עולם ינעל העולם", ":)"],
        ["Hello"],
        ["World"]
        ]
        """

        rows = infoList
        service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID,
            range="Sheet1!A:Z",
            body={
                "majorDimension": "ROWS",
                "values": rows
            },
            valueInputOption="USER_ENTERED"
        ).execute()
        #result = sheets.values().get(spreadsheetId = SPREADSHEET_ID, range)
    except:
        print("error")
        pass

if __name__ == "__main__":
    googleSheetsWriter([
        ["Jul 11 2023", "826.73", "783.39", "421.7", "2,031.82", "18.59", "87", "21.13", "156", "1.79"],
        ["", "0", "0", "18.59"],
        ["", "0", "0", "0"]
    ])