from django.urls import path
from .views import signup, student_login, custom_logout, home
from django.contrib.auth import views as auth_views
urlpatterns =[
    path("", home, name='home'),
    path("signup/", signup, name='signup'),
    path("student-login/", student_login, name="student-login"),
    path('logout/', custom_logout, name='custom_logout'),
]