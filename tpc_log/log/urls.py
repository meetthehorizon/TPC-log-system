from django.urls import path
from .views import logview
urlpatterns =[
    path("logview/", logview, name='logview')
]