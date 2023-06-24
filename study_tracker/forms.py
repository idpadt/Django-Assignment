from django.forms import ModelForm
from study_tracker.models import Assignment

class AssignmentRecordForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ["name", "subject", "progress", "description"]