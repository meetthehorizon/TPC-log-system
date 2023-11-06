from django.urls import path
from .views import logview
urlpatterns =[
    path("logview/<int:process_id>", logview, name='logview')
]