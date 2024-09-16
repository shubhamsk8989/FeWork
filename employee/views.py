from django.shortcuts import render,redirect
from employer.models import Employer, create_job
from employee.models import Employee, FormFill

from . import models
from. import forms
from django.contrib import messages
from django.http import HttpResponse
from employee.functions import handle_uploaded_file  


# Create your views here.
def employee_home(request):
    user=request.user
    job_post=create_job.objects.all()
    employee = models.Employee.objects.filter(user=request.user).first()
    return render(request,'employee_home.html',{'user':user,'job_post':job_post,'employee':employee})


def about_job(request, user, jobid):
    job_post=create_job.objects.get(id=jobid)

    employee = models.Employee.objects.filter(user=request.user).first()
    # employee = Employee.objects.filter(id=employee1).first()
    job = models.create_job.objects.filter(id=jobid).first()
    filled=FormFill.objects.filter(job_id=job,employee_id=employee )
    # myApplications=create_job.objects.get(id=jobid)
    

    return render(request,'employee_about_job.html',{'user':user,'jobid':jobid,'job_post':job_post,'filled':filled, 'job':job})


def form_filling(request, user, jobid):
    jobform=forms.FillForm()
    job = models.create_job.objects.filter(id=jobid).first()
    print(models.Employee.id)
    if request.method=='POST': 
        jobform=forms.FillForm(request.POST,request.FILES)
        if jobform.is_valid():
            qform1=jobform.save(commit=False)
            file_path=handle_uploaded_file(request.FILES['resume'])

            employee = models.Employee.objects.filter(user=request.user).first()
            job = models.create_job.objects.filter(id=jobid).first()
            print(employee)
            print(job)
            qform1.employee_id=employee
            qform1.job_id=job
            qform1.save()
            return redirect('employee:employee_home') 
        else:
            messages.error(request, "Please fill in the inputs correctly.")
            return HttpResponse("<script>alert('Please fill in the inputs correctly');window.location.href = window.location.href;</script>")

    return render(request,'employee_form_filling.html',{'user':user,'jobform':jobform,'jobid':jobid, 'job':job})




def view_application_history(request,employeeid):
    myApplications=FormFill.objects.filter(employee_id=employeeid)
    
    return render(request,'employee_view_application_history.html',{'myApplications':myApplications})
# def fill_form(request):
#     jobform=forms.CreateJob()
#     if request.method=='POST': 
#         jobform=forms.CreateJob(request.POST)
#         if jobform.is_valid():
#             qform1=jobform.save(commit=False)
#             employer = models.User.objects.filter(username=request.user).first()
#             qform1.employer_id=employer
#             qform1.save()
#             return redirect('employer:employer_home') 
#     return render(request,'employee_fill_form.html',{})
