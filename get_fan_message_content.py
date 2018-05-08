from contentful import Client
import os

SPACE_ID = os.getenv('CONTENTFUL_SPACE_ID')
ACCESS_TOKEN = os.getenv('CONTENTFUL_ACCESS_TOKEN')
ENTRY_ID = os.getenv('CONTENTFUL_FAN_MESSAGE_ENTRY_ID')

def get_fan_message_content():
    client = Client(SPACE_ID, ACCESS_TOKEN)
    entry = client.entry(ENTRY_ID)

    message_to_fans = entry.fan_message

    return (message_to_fans)
