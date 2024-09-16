from django.urls import path
from . import views

app_name='employer'

urlpatterns = [
        path('employer_home/', views.employer_home, name = 'employer_home'),
        path('create_job/', views.create_job, name = 'create_job'),
        path('my_jobs/<int:user>', views.my_jobs, name = 'my_jobs'),
        path('viewApplicants/<int:employerid>/<int:jobid>/', views.viewApplicants, name = 'viewApplicants'),
        path('select_form/<int:employeeid>/<int:jobid>/', views.select_form, name = 'select_form'),
        path('reject_form/<int:employeeid>/<int:jobid>/', views.reject_form, name = 'reject_form'),

        path('view_application_details/<int:employeeid>/<int:jobid>/', views.view_application_details, name = 'view_application_details'),

]

