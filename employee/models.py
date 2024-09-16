from django.db import models
from django.contrib.auth.models import User
from employer.models import Employer,create_job

# Create models here.
class Employee(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)  # Adding phone number field
    interested_domain=models.CharField(max_length=30, default='')
    city=models.CharField(max_length=50, default='')
    
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
    
class FormFill(models.Model):
    job_id = models.ForeignKey(create_job, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    formfilling_date=models.DateField(auto_now=True)
    expected_delivery=models.IntegerField(default=0)
    est_budget = models.IntegerField(blank=True,default=0)
    resume=models.FileField(upload_to='static/resume/')
    message=models.CharField(max_length=500, blank=True)
    status=models.CharField(max_length=30, default='pending')  #pending, selected, not selected

    def select_form(self):
        if self.status=='pending':
            self.status='selected'
            self.save()
    def reject_form(self):
        if self.status=='pending':
            self.status='rejected'
            self.save()

