from django.db import models
from users.models import User

'''
The below list of tuples represents the choices for the status field in the
OutageReport model. The status field is a CharField that can be one of the
following choices: 'reported', 'in_progress', or 'resolved'. The default status
is 'reported'.
'''
STATUS_CHOICES = (
    ('reported', 'Reported'),
    ('in_progress', 'In Progress'),
    ('resolved', 'Resolved'),
)

'''
The OutageReport model represents the outage reports that users and admins
submit. The model has the following fields:
- report_id: an AutoField that serves as the primary key for the model
- user_id: a ForeignKey that links the OutageReport model to the User model
- report_date: a DateTimeField that stores the date and time the report was submitted
- location: a CharField that stores the location of the outage
- description: a TextField that stores a detailed description of the outage
- status: a CharField that stores the status of the outage report
- planned: a BooleanField that indicates whether the outage is planned or not
- estimated_restoration_time: a DateTimeField that stores the estimated time for restoration
'''
class OutageReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    report_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='reported')
    planned = models.BooleanField(default=False)
    estimated_restoration_time = models.DateTimeField()

    def __str__(self):
        return f"Outage {self.report_id} by {self.user_id.username}"