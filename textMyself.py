#!/usr/bin/env python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.


# Preset values:
accountSID = 'ACbf3b25230d448fd46de46f5306b2b6e7'
authToken = '74e04962257e6c6a3594bfc0fe0acea1'
myNumber = '+15073228190'
twilioNumber = '+17755355885'

from twilio.rest import Client


def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
