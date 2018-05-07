from twilio.rest import Client
import os

def sendFanMessage(fan_message):
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    client.api.account.messages.create(
        to="+4917689272395",
        from_="+4915735989263",
        body=fan_message)
