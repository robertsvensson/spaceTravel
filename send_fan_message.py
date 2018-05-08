from twilio.rest import Client
import os

def send_fan_message(fan_message):
    ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    client.api.account.messages.create(
        to="+4917689272395",
        from_="+4915735989263",
        body=fan_message)
