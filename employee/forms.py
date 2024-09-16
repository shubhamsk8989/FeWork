from django import forms
from django.contrib.auth.models import User
from . import models

class FillForm(forms.ModelForm):
    class Meta:
        model=models.FormFill
        fields=['expected_delivery','est_budget','resume','message']
