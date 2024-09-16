from django.contrib import admin
from django.urls import path, include
from website import views
from django.contrib.auth.views import LoginView, LogoutView

app_name='website'
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.index, name = 'index'),
    path('about/', views.about, name='about'),
    path('project_scope', views.project_scope, name='project_scope'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('admin_home', LoginView.as_view(template_name='admin_home.html'), name = 'admin_home'),
    path('admin_employee', views.admin_employee, name = 'admin_employee'),
    path('admin_employer', views.admin_employer, name = 'admin_employer'),
    path('admin_jobs', views.admin_jobs, name = 'admin_jobs'),
    path('admin_selections', views.admin_selections, name = 'admin_selections'),

    path('logout/', LogoutView.as_view(next_page='website:signin'), name='logout'),

    path('signin/', views.signin, name = 'signin'),
    path('afterlogin/', views.afterlogin, name = 'afterlogin'),
    path('employee_signup/', views.EmployeeSignup, name = 'employee_signup'),
    path('employer_signup/', views.EmployerSignup, name = 'employer_signup'),
    path('delete_employee',views.delete_employee, name="delete_employee"),
    path('edit_employee/<int:employee_id>',views.edit_employee, name="edit_employee"),
    path('add_employee',views.add_employee, name="add_employee"),
    
    path('delete_employer',views.delete_employer, name="delete_employer"),
    path('edit_employer/<int:employer_id>',views.edit_employer, name="edit_employer"),
    path('add_employer',views.add_employer, name="add_employer"),
    path('delete_job',views.delete_job, name="delete_job"),


]