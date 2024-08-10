from django import forms
from .models import OutageReport

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

        