from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import OutageReport
from .forms import OutageReportForm


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