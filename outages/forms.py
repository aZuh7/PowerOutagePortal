from django import forms
from .models import OutageReport, STATUS_CHOICES

class OutageReportForm(forms.ModelForm):
    class Meta: 
        model = OutageReport
        fields = ['location', 'description', 'planned', 'estimated_restoration_time']

    def __init__(self, *args, **kwargs):
        is_admin = kwargs.pop('is_admin', False)
        is_update = kwargs.pop('is_update', False)
        super(OutageReportForm, self).__init__(*args, **kwargs)

        if is_admin and not is_update:
            self.fields['status'] = forms.ChoiceField(choices=OutageReport.STATUS_CHOICES, disabled=not is_admin)

class FilterOutageReport(forms.Form):
    report_id = forms.IntegerField(required=False, label='Report ID')
    status = forms.ChoiceField(choices=[('', 'All')] + list(STATUS_CHOICES), required=False, label='Status')
    planned = forms.ChoiceField(choices=[('', 'All'), ('True', 'Yes'), ('False', 'No')], required=False, label='Planned')

    def __init__(self, *args, **kwargs):
        super(FilterOutageReport, self).__init__(*args, **kwargs)
        self.fields['status'].label = 'Filter by Status'
        self.fields['planned'].label = 'Filter by Planned'
        self.fields['report_id'].label = 'Filter by Report ID'