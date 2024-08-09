from django.shortcuts import render
from .models import VonageAPI, SendGrid
from .outages.models import OutageReport

# Create your views here.
def send_notification(request):
    pass

def send_sms(request):
    pass

def send_email(request):
    sg = SendGrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

    from_email = OutageReport.objects.get(user_id=request.user).email

        if request == "Outage report submitted successfully."
            SendGrid.submission_subject = "Outage Report Submitted"
            SendGrid.submission_content = "Your outage report has been submitted successfully."
            sg.send(SendGrid.from_email, SendGrid.to_email, SendGrid.submission_subject, SendGrid.submission_content)


    pass