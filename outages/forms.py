from django import forms
from .models import OutageReport

class OutageReportForm(forms.ModelForm):
    class Meta: 
        model = OutageReport
        fields = ['location', 'description', 'status', 'planned', 'estimated_restoration_time']
        