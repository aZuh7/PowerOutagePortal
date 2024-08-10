from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from outages.models import OutageReport

'''
This is a view function that renders the user dashboard html template.
Here we also predefine variables to be returned if the user wants to view their previously submitted reports.
'''
@login_required
def user_dashboard(request):
    view_reports = request.GET.get('view_reports') == 'true'
    user_reports = OutageReport.objects.filter(user_id=request.user) if view_reports else None

    return render(request, 'dashboard/user_dashboard.html', {
        "view_reports": view_reports,
        "reports": user_reports})

'''
This view function renders the admin dashboard html template.
'''
@login_required
def admin_dashboard(request):
    options = [
        "Report an Outage",
        "View all Outage Reports",
        "Generate Reports",
        "Calculate Outages by Zip Codes"
    ]
    return render(request, 'dashboard/admin_dashboard.html', {"options": options})