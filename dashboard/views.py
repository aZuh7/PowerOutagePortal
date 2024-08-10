from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def user_dashboard(request):
    view_reports = request.GET.get('view_reports') == 'true'
    user_reports = OutageReport.objects.filter(user_id=request.user) if view_reports else None


    return render(request, 'dashboard/user_dashboard.html', {
        "view_reports": view_reports,
        "reports": user_reports})

@login_required
def admin_dashboard(request):
    options = [
        "Report an Outage",
        "View all Outage Reports",
        "Generate Reports",
        "Calculate Outages by Zip Codes"
    ]
    return render(request, 'dashboard/admin_dashboard.html', {"options": options})