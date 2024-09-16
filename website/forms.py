from django import forms
from django.contrib.auth.models import User
from employer.models import Employer
from employee.models import Employee


class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'styled-input','id':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'styled-input','id':'password'}))


class EmployerUserSignup(forms.ModelForm):
    
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        error_messages = {
            'first_name': {'required': 'Please enter your first name'},
            'last_name': {'required': 'Please enter your last name'},
        }

class EmployerSignup(forms.ModelForm):
    class Meta:
        model=Employer
        fields=['Address','Company_name','phone_number']


class EmployeeUserSignup(forms.ModelForm):
    interested_domain=forms.CharField( max_length=30, required=True)
    city=forms.CharField(max_length=50, required=True)
    phone_number = forms.CharField(max_length=15)  # Adding phone number field

    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        error_messages = {
            'first_name': {'required': 'Please enter your first name'},
            'last_name': {'required': 'Please enter your last name'},
        }


class EmployeeSignup(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['city','interested_domain','phone_number']



class EditEmployeeUserForm(forms.ModelForm):
    interested_domain=forms.CharField( max_length=30, required=True)
    city=forms.CharField(max_length=50, required=True)
    phone_number = forms.CharField(max_length=15)  # Adding phone number field

    class Meta:
        model=User
        fields=['first_name','last_name','username','email']
        
        error_messages = {
            'first_name': {'required': 'Please enter your first name'},
            'last_name': {'required': 'Please enter your last name'},
        }

class EditEmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['city','interested_domain','phone_number']


class EditEmployerUserForm(forms.ModelForm):
   
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']
        
        error_messages = {
            'first_name': {'required': 'Please enter your first name'},
            'last_name': {'required': 'Please enter your last name'},
        }

class EditEmployerForm(forms.ModelForm):
    class Meta:
        model=Employer
        fields=['Address','Company_name','phone_number']



