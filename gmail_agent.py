import os
import base64
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from agno.agent import Agent
from agno.models.google import Gemini

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API")

# Setup scopes and Gmail API client
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

# Gemini agent for summarization
summary_agent = Agent(
    model=Gemini(id="gemini-1.5-flash", api_key=GEMINI_API_KEY),
    description="You are an assistant that summarizes Gmail emails and extracts tasks or deadlines.",
    markdown=True
)

def summarize_email_content(content):
    prompt = f"""
Summarize the following email and list any tasks or deadlines mentioned in it:

Email:
{content}
"""
    return summary_agent.print_response(prompt, stream=False)

def get_and_summarize_emails(service, num_emails=5):
    results = service.users().messages().list(userId='me', maxResults=num_emails).execute()
    messages = results.get('messages', [])

    summaries = []
    for i, message in enumerate(messages):
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        payload = msg.get('payload', {})
        headers = payload.get("headers", [])

        # Extract Subject
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "(No Subject)")

        # Get email body
        parts = payload.get("parts", [])
        body = ""
        if parts:
            for part in parts:
                if part['mimeType'] == 'text/plain':
                    data = part['body']['data']
                    body = base64.urlsafe_b64decode(data).decode('utf-8')
                    break

        if body:
            summary = summarize_email_content(body)
            summaries.append({"subject": subject, "summary": summary})
        else:
            summaries.append({"subject": subject, "summary": "No readable content."})
    return summaries
