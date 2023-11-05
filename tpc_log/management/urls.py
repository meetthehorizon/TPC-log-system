from django.urls import path
from .views import CompanyList, CompanyEnlist, CompanyEdit, CompanyDelete

urlpatterns = [
    path('company/', CompanyList, name='company_list'),
    path('company/add/', CompanyEnlist, name='company_enlist'),
    path('company/<int:company_id>/edit/', CompanyEdit, name='company_edit'),
    path('company/<int:company_id>/confirm_delete/', CompanyDelete, name='company_delete'),
]
