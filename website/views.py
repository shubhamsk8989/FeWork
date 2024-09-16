from . import forms
from django.contrib.auth.models import User, Group
from employee.models import Employee, FormFill
from employer.models import Employer, create_job

from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def project_scope(request):
    return render(request, 'project_scope.html')

def contact_us(request):
    return render(request, 'contact_us.html')


def signin(request):
    if request.method == 'POST':
        form = forms.SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('website:afterlogin')  # Redirect to user home page after login
            else:
                pass
    else:
        form = forms.SignInForm()
    
    return render(request, 'signin.html', {'form': form})

def is_employee(user):
    return user.groups.filter(name='Employee').exists()

def is_employer(user):
    return user.groups.filter(name='Employer').exists()


@login_required(login_url='website:signin') #login_url='home'
@never_cache
def afterlogin(request):
    if is_employee(request.user):
        return redirect('employee:employee_home')
    elif is_employer(request.user):
        return redirect('employer:employer_home')
    else:
        jobs=create_job.objects.all()
        current_job=create_job.objects.filter(status='live')
        employer=Employer.objects.all()
        employee=Employee.objects.all()
        applications=FormFill.objects.all()
        selected=FormFill.objects.filter(status='selected')
        print(jobs)
        return render(request,'admin_home.html',{'job_count':len(jobs),'employer_count':len(employer),'employee_count':len(employee),'application_count':len(applications),'selection_count':len(selected),'current_job_count':len(current_job)})

def EmployeeSignup(request):
    employeeform=forms.EmployeeSignup()
    userform=forms.EmployeeUserSignup()
    if request.method=='POST':
        employeeform=forms.EmployeeSignup(request.POST)
        userform=forms.EmployeeUserSignup(request.POST)

        if employeeform.is_valid() and userform.is_valid():
            user=userform.save()
            user.set_password(user.password)
            user.save()

            employee=employeeform.save(commit=False)
            employee.user=user
            employee.save()
            employee_group = Group.objects.get_or_create(name='Employee')
            employee_group[0].user_set.add(user)
            return redirect('website:signin')
        else:
            error=employeeform.errors
    return render(request, 'employee_signup.html',{'employeeform':employeeform,'userform':userform})


def EmployerSignup(request):
    employerform=forms.EmployerSignup()
    userform=forms.EmployerUserSignup()

    if request.method=='POST':
        employerform=forms.EmployerSignup(request.POST)
        userform=forms.EmployerUserSignup(request.POST)

        if employerform.is_valid() and userform.is_valid():
            user=userform.save()
            user.set_password(user.password)
            user.save()

            employer=employerform.save(commit=False)
            employer.user=user
            employer.save()
            employer_group = Group.objects.get_or_create(name='Employer')
            employer_group[0].user_set.add(user)
            return redirect('website:signin')
        else:
            error=employerform.errors
    return render(request, 'employer_signup.html',{'employerform':employerform,'userform':userform})


def admin_employee(request):
    employee=Employee.objects.all()

    return render(request, 'admin_employee.html',{'employee':employee})


def admin_employer(request):
    employer=Employer.objects.all()

    return render(request, 'admin_employer.html',{'employer':employer})



def admin_jobs(request):
    jobs=create_job.objects.all()
    return render(request, 'admin_jobs.html',{'jobs':jobs})



def admin_selections(request):
    selected=FormFill.objects.filter(status='selected')
    return render(request, 'admin_selections.html',{'selected':selected})


def delete_employee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        if employee_id:
            Employee.objects.filter(id=employee_id).delete()
            return redirect('website:admin_employee')
        
def edit_employee(request,employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    user=get_object_or_404(User, username=employee.user)
    if request.method == 'POST':
        form = forms.EditEmployeeForm(request.POST, instance=employee)
        userform=forms.EditEmployeeUserForm(request.POST, instance=user)
        print(userform)
        if form.is_valid() and userform.is_valid():
            userform.save()
            form.save()
            return redirect('website:admin_employee')  # Redirect to a success page
    else:
        form = forms.EditEmployeeForm(instance=employee)
    employee_details=Employee.objects.get(id=employee_id)
    return render(request, 'admin_edit_employee.html',{'form':form,'employee_details':employee_details})


def add_employee(request):
    employeeform=forms.EmployeeSignup()
    userform=forms.EmployeeUserSignup()
    if request.method=='POST':
        employeeform=forms.EmployeeSignup(request.POST)
        userform=forms.EmployeeUserSignup(request.POST)

        if employeeform.is_valid() and userform.is_valid():
            user=userform.save()
            user.set_password(user.password)
            user.save()

            employee=employeeform.save(commit=False)
            employee.user=user
            employee.save()
            employee_group = Group.objects.get_or_create(name='Employee')
            employee_group[0].user_set.add(user)
            return redirect('website:admin_employee')
        else:
            error=employeeform.errors
    return render(request, 'admin_add_employee.html',{'employeeform':employeeform,'userform':userform})


# employer
def delete_employer(request):
    if request.method == 'POST':
        employer_id = request.POST.get('employer_id')
        if employer_id:
            Employer.objects.filter(id=employer_id).delete()
            return redirect('website:admin_employer')
        
def edit_employer(request,employer_id):
    employer = get_object_or_404(Employer, pk=employer_id)
    user=get_object_or_404(User, username=employer.user)
    if request.method == 'POST':
        form = forms.EditEmployerForm(request.POST, instance=employer)
        userform=forms.EditEmployerUserForm(request.POST, instance=user)
        print(userform)
        if form.is_valid() and userform.is_valid():
            print('hii')
            userform.save()
            form.save()
            return redirect('website:admin_employer')  # Redirect to a success page
    else:
        form = forms.EditEmployerForm(instance=employer)
    employer_details=Employer.objects.get(id=employer_id)
    return render(request, 'admin_edit_employer.html',{'form':form,'employer_details':employer_details})


def add_employer(request):
    employerform=forms.EmployerSignup()
    userform=forms.EmployerUserSignup()
    if request.method=='POST':
        employerform=forms.EmployerSignup(request.POST)
        userform=forms.EmployerUserSignup(request.POST)

        if employerform.is_valid() and userform.is_valid():
            user=userform.save()
            user.set_password(user.password)
            user.save()

            employer=employerform.save(commit=False)
            employer.user=user
            employer.save()
            employer_group = Group.objects.get_or_create(name='Employer')
            employer_group[0].user_set.add(user)
            return redirect('website:admin_employer')
        else:
            error=employerform.errors
    return render(request, 'admin_add_employer.html',{'employerform':employerform,'userform':userform})



def delete_job(request):
    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        if job_id:
            create_job.objects.filter(id=job_id).delete()
            return redirect('website:admin_jobs')
