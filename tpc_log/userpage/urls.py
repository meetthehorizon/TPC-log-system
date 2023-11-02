from django.urls import path
from .views import duties_view, userinfo
urlpatterns =[
    path("duties/", duties_view, name='duties'),
    path("userinfo/", userinfo, name='userinfo'),
    path("", userinfo, name='userinfo_dashboard'),
    

]