from django.shortcuts import render, redirect,get_object_or_404
from . import forms
from . import models
from employee.models import Employee,FormFill
from employer.models import Employer


# Create your views here.
def employer_home(request):
    user=request.user
    employer = models.Employer.objects.filter(user=request.user).first()
    print(employer)
    return render(request,'employer_home.html',{'user':user, 'employer':employer})


def create_job(request):
    jobform=forms.CreateJob()
    if request.method=='POST': 
        jobform=forms.CreateJob(request.POST)
        if jobform.is_valid():
            qform1=jobform.save(commit=False)
            employer = models.Employer.objects.filter(user=request.user).first()
            qform1.employer_id=employer
            qform1.save()
            return redirect('employer:employer_home') 
    return render(request,'employer_create_job.html',{'jobform':jobform})

def my_jobs(request,user):
    employer = models.Employer.objects.filter(user=request.user).first()
    jobs=models.create_job.objects.filter(employer_id=employer)
    return render(request,'employer_my_job.html',{'jobs':jobs,'employer':employer})


def viewApplicants(request, employerid, jobid):
    employer = models.Employer.objects.filter(user=request.user).first()
    job = models.create_job.objects.filter(id=jobid).first()
    applications=FormFill.objects.filter(job_id=job)
    # a=FormFill.objects.filter(job_id=job)

    return render(request,'employer_view_applicants.html',{'applications':applications,'employer':employer,'job':job})


def select_form(request,employeeid,jobid):
    employer = models.Employer.objects.filter(user=request.user).first()
    job = models.create_job.objects.filter(employer_id=employer).first()
    applications=FormFill.objects.filter(job_id=job)
    form=get_object_or_404(FormFill, employee_id=employeeid, job_id=jobid)
    form.select_form()
    return render(request,'employer_view_applicants.html',{'applications':applications,'employer':employer})

def reject_form(request,employeeid,jobid):
    employer = models.Employer.objects.filter(user=request.user).first()
    job = models.create_job.objects.filter(employer_id=employer).first()
    applications=FormFill.objects.filter(job_id=job)
    form=get_object_or_404(FormFill, employee_id=employeeid, job_id=jobid)
    form.reject_form()
    return render(request,'employer_view_applicants.html',{'applications':applications,'employer':employer})

def view_application_details(request,employeeid,jobid):
    employee = Employee.objects.filter(id=employeeid).first()
    job = models.create_job.objects.filter(id=jobid).first()
    applications=FormFill.objects.filter(job_id=job,employee_id=employee )
    return render(request,'employer_view_application_details.html',{'applications':applications, 'job': job})
