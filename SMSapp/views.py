from django.shortcuts import render
from twilio.rest import Client
from django.conf import settings                                                                                                                                                       
from django.http import HttpResponse


# Create your views here.

def broadcast_sms(request):
    message_to_broadcast = ("How are you")
    client = Client(settings.TWILLIO_ACCOUNT_SID, settings.TWILLIO_AUTH_TOKEN)
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        print(recipient)
        if recipient:
            client.messages.create(to=recipient,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)
    return HttpResponse("messages sent!"+ message_to_broadcast, 200)
