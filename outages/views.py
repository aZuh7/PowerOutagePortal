from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import OutageReport
from .forms import OutageReportForm
from .forms import OutageUpdateForm
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
    return render(request, 'outages/outage_report_form.html', {'form': form})

@login_required
def update_outage_report(request):
    # Don't forget to incorporate trigger function for notifications
    if request.method == 'POST':
        form = OutageUpdateForm(request.POST)
        if form.is_valid():
         OutageReport = form.save(commit=False)
         OutageReport.report_id = request.user
         OutageReport.save()

        # Attempt to send notifications
        sms_sent = TwilioSMS.send_notification(OutageReport)
        email_sent = DjangoSMTP.send_notification(OutageReport)
            
            # Check if both notifications were sent successfully
        if sms_sent and email_sent:
                message = 'Notifications Sent Successfully'
        elif sms_sent:
                message = 'SMS Notification Sent.'
        elif email_sent:
                message = 'Email Notification Sent'
        else:
                message = 'Notifications Failed'
            
        return redirect('admin_dashboard', message=message)
    else:
        form=OutageUpdateForm()

    return redirect(request, 'admin_dashboard', 'Outage Report Updated Effectively')

    pass

@login_required
def get_user_outage_report(request, **extra_kwargs):
    user_reports = OutageReport.objects.filter(user_id=request.user)
    reports_list= dict(user_reports)
    return render(request,'user_outage_reports.html',{'user_reports': reports_list}) 



@login_required
def get_all_outage_reports(request):

    print(f"User Type: {request.user.user_type}")  # Debugging line
    if request.user.user_type != 'admin':
        # If the user is not an admin, raise a permission denied error
        raise PermissionDenied("You do not have permission to view this page.")
    
    # Retrieve all outage reports
    outage_reports = OutageReport.objects.all()

    #Filter by report ID if provided in request
    report_id = request.GET.get('report_id')
    if report_id:
        try:
            report_id = int(report_id)
            outage_reports = outage_reports.filter(report_id=report_id)
        except ValueError:

            pass
    # Pass the outage reports to the template
    return render(request, 'admin_dashboard.html', {'outage_reports': outage_reports})



export = report_outage
