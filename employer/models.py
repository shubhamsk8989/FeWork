from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    Address=models.CharField(max_length=100, default='')
    Company_name=models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15)  # Adding phone number field

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    
    @property
    def email(self):
        return self.user.email

    @property
    def get_instance(self):
        return self
    
    def __str__(self):
        return self.user.first_name
    
class create_job(models.Model):
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    job_heading = models.CharField(max_length=500, default='na', null=False)
    job_description = models.CharField(max_length=5000, default='no description')
    job_domain = models.CharField(max_length=50, default='not provided')
    upload_date=models.DateField(auto_now=True)
    due_date=models.DateField(blank=True)
    est_budget = models.IntegerField(blank=True)
    status=models.CharField(max_length=30, default='live')
