from django.shortcuts import render
from .models import VonageAPI, SendGrid
from outages.models import OutageReport
from django.contrib.auth.decorators import login_required

import os
import vonage
# Create your views here.
@login_required
def send_notification(request):
    

    pass

@login_required
def send_sms(request):
    client = vonage.Client(VonageAPI.VONAGE_API_KEY,VonageAPI.VONAGE_API_SECRECT)


    sms = vonage.sms(client)
    responseData = client.sms.send_message(
    {
        "from": VonageAPI.VONAGE_BRAND_NAME,
        "to": VonageAPI.TO_NUMBER,
        "text": "You have a new notification",
    }
)

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

    pass

@login_required
def send_email(request):
    pass