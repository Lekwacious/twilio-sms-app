from django.shortcuts import render
from twilio.rest import Client
from django.conf import settings                                                                                                                                                     
from django.http import HttpResponse
from datetime import datetime, timedelta
from redis import Redis
from rq import Queue

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'SMSserviceproject.settings'

q = Queue(connection=Redis())



# Create your views here.


def send_sms(from_, to, body):
    client = Client(settings.TWILLIO_ACCOUNT_SID, settings.TWILLIO_AUTH_TOKEN)
    client.messages.create(from_=from_, to=to, body=body)

def broadcast_sms(request):
    message_to_broadcast = ("How are you")
    delta = 0

    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        print(recipient)
        if recipient:
            q.enqueue_in(timedelta(seconds=delta), send_sms, settings.TWILIO_NUMBER, recipient, message_to_broadcast)
            delta += 15
    return HttpResponse("messages sent!"+ message_to_broadcast, 200)
