from django.urls import path
from .views import report_outage, update_outage_report, get_user_outage_report, get_all_outage_reports

urlpatterns = [
    path('report/', report_outage, name='report_outage'),
    path('update/<int:report_id>/', update_outage_report, name='update_outage_report'),
    path('my_reports/', get_user_outage_report, name='get_user_outage_reports'),
    path('all_reports/', get_all_outage_reports, name='get_all_outage_reports'),
]