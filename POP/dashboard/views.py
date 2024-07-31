from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def user_dashboard(request):
    return render(request, 'dashboard/user_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')