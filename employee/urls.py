from django.urls import path
from . import views
app_name='employee'


urlpatterns = [
        path('employee_home/', views.employee_home, name = 'employee_home'),
        path('form_filling/<str:user>/<int:jobid>/', views.form_filling, name = 'form_filling'),
        path('about_job/<str:user>/<int:jobid>/', views.about_job, name = 'about_job'),
        path('view_application_history/<int:employeeid>/', views.view_application_history, name = 'view_application_history'),

]
