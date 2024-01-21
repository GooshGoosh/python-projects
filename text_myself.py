'''
text_myself.py - Defines a function to send a message to a phone number.
'''

from twilio.rest import Client


ACCOUNT_SID = ''
AUTH_TOKEN = ''
MY_NUMBER = ''
TWILIO_NUMBER = ''


def text_myself(message):
    """text_myself Sends a message to the from/to the specified number.

    Args:
        message (str): The message to send to the phone number.
    """
    twilio_cli = Client(ACCOUNT_SID, AUTH_TOKEN)
    twilio_cli.messages.create(body=message, from_=TWILIO_NUMBER, to=MY_NUMBER)
