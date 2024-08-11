from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import OutageReport
from .forms import OutageReportForm, FilterOutageReport

'''
The following function is a view function that loads the outage report form. 
Once the user or admin fills out the form and clicks the submit button, the 
function receives the POST request, validates the form data, saves the
data to the database and renders an outage confirmation page.
'''
@login_required
def report_outage(request): 
    if request.method == 'POST':
        form = OutageReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user_id = request.user
            report.save()
            return render(request, 'outages/outage_confirmation.html')
        
    else:
        form = OutageReportForm()
    return render(request, 'outages/outage_report_form.html', {'form': form})

'''
The following function is a view function that updates an outage report.
'''
@login_required
def update_outage_report(request, report_id):
    # Don't forget to incorporate trigger function for notifications
    try:
        report = OutageReport.objects.get(pk = report_id)
    except OutageReport.DoesNotExist:
        pass
    if request.method == 'POST':
        form = OutageReportForm(request.POST, instance = report)
        if form.is_valid():
            form.save()
            # notify_users(report)
    else:
        form = OutageReport(instance = report)
    return render(request, 'outages/update_outage_report.html', {'form': form})


'''
The following function is a view function that deletes an outage report.
'''

@login_required
def get_user_outage_report(request, **extra_kwargs):
    user_reports = OutageReport.objects.filter(user_id=request.user)
    return render(request, 'outages/user_outage_reports.html', {'user_reports': user_reports})

'''
The following function is a view function that retrieves all outage reports.
'''

@login_required
def get_all_outage_reports(request):
    if request.user.user_type == 'admin':
        form = FilterOutageReport(request.GET)
        reports = OutageReport.objects.all()

        if form.is_valid():
            report_id = form.cleaned_data.get('report_id')
            if report_id:
                reports = reports.filter(report_id=report_id)
            status = form.cleaned_data.get('status')
            if status:
                reports = reports.filter(status=status)
            planned = form.cleaned_data.get('planned')
            if planned:
                reports = reports.filter(planned=(planned == 'True'))
    return render(request, 'dashboard/admin_dashboard.html', {'reports': reports, 'form': form})
