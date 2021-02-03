from __future__ import print_function
import pickle, os.path, re
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import datetime, timezone, timedelta
from os import getenv

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_latest_code():
    CODE_EMAIL_SENDER = getenv('CODE_EMAIL_SENDER')
    CODE_EMAIL_SUBJECT = getenv('CODE_EMAIL_SUBJECT')

    CODE_REGEX = getenv('CODE_REGEX')

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'google-credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    results = service.users().messages().list(userId='me', q=f"from:{CODE_EMAIL_SENDER} subject:'{CODE_EMAIL_SUBJECT}'", maxResults=1).execute()
    message = service.users().messages().get(userId='me', id=results['messages'][0]['id']).execute()

    login_code = re.search(CODE_REGEX, message['snippet']).group(0)
    time = datetime.fromtimestamp(int(message['internalDate'][:-3])).strftime("%d %b, %H:%M:%S")

    return login_code, time
