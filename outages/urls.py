from django.urls import path
from .views import report_outage, update_outage_report, get_user_outage_report, get_all_outage_reports

urlpatterns = [
    path('report/', report_outage, name='report_outage'),
]