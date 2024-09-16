from django import forms
from django.contrib.auth.models import User
from . import models

class CreateJob(forms.ModelForm):
    class Meta:
        model=models.create_job
        fields=['job_heading','job_description','job_domain','due_date','est_budget']
