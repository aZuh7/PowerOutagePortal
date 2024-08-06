from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import OutageReport
from .forms import OutageReportForm
from notifications.models import TwilioSMS, DjangoSMTP


# Create your views here.
@login_required
def report_outage(request):
    if request.method == 'POST':
        form = OutageReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user_id = request.user
            report.save()
            return redirect('outages:outage_reported')
    else:
        form = OutageReportForm()
    return render(request, 'outages/report_outage.html', {'form': form})

@login_required
def update_outage_report(request):
    # Don't forget to incorporate trigger function for notifications
    pass

def get_user_outage_report(request, **extra_kwargs):
    user_reports = OutageReport.objects.filter(user_id=request.user)
    return 

def get_all_outage_reports():
    pass