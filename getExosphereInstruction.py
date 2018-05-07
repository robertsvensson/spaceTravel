from contentful import Client
import os

SPACE_ID = os.getenv('CONTENTFUL_SPACE_ID')
ACCESS_TOKEN = os.getenv('CONTENTFUL_ACCESS_TOKEN')
ENTRY_ID = os.getenv('CONTENTFUL_EXOSPHERE_ENTRY_ID')

def getExosphereInstruction(username):
    client = Client(SPACE_ID, ACCESS_TOKEN)

    if username == 'habibi':
        entry = client.entry(ENTRY_ID,{'locale': 'sw'})
    elif username == 'laura':
        entry = client.entry(ENTRY_ID,{'locale': 'de'})
    else:
        entry = client.entry(ENTRY_ID)

    exosphere_instruction = entry.exosphere_instruction

    return ({'exosphere_instruction':exosphere_instruction})
