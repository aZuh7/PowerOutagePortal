from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def user_dashboard(request):
    options = [
        "Report an Outage",
        "View my Outage Reports"
    ]
    return render(request, 'dashboard/user_dashboard.html', {"options": options})

@login_required
def admin_dashboard(request):
    options = [
        "Report an Outage",
        "View all Outage Reports",
        "Generate Reports",
        "Calculate Outages by Zip Codes"
    ]
    return render(request, 'dashboard/admin_dashboard.html', {"options": options})