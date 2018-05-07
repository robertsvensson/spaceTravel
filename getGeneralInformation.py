from contentful import Client
import os

SPACE_ID = os.getenv('CONTENTFUL_SPACE_ID')
ACCESS_TOKEN = os.getenv('CONTENTFUL_ACCESS_TOKEN')
ENTRY_ID = os.getenv('CONTENTFUL_GENERAL_INFORMATION')

def getGeneralInformation():
    client = Client(SPACE_ID, ACCESS_TOKEN)
    entry = client.entry(ENTRY_ID)

    greeting_title = entry.greeting_title
    greeting_message = entry.greeting_message
    greeting_sender = entry.greeting_sender

    return ({'greeting_title':greeting_title, 'greeting_message': greeting_message, 'greeting_sender': greeting_sender})
