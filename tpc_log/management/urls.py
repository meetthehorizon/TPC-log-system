from django.urls import path
from .views import CompanyList, CompanyEnlist, CompanyEdit, CompanyDelete, ProcessList, ProcessEnlist, ProcessEdit, ProcessDelete, DutyList, DutyEnlist, DutyEdit, DutyDelete, ShortlistList, ShortlistEnlist, ShortlistEdit, ShortlistDelete

urlpatterns = [
    path('company/', CompanyList, name='company_list'),
    path('company/add/', CompanyEnlist, name='company_enlist'),
    path('company/<int:company_id>/edit/', CompanyEdit, name='company_edit'),
    path('company/<int:company_id>/confirm_delete/', CompanyDelete, name='company_delete'),
    path('process/', ProcessList, name='process_list'),
    path('process/add/', ProcessEnlist, name='process_enlist'),
    path('process/<int:process_id>/edit/', ProcessEdit, name='process_edit'),
    path('process/<int:process_id>/confirm_delete/', ProcessDelete, name='process_delete'),
    path('duty/', DutyList, name='duty_list'),
    path('duty/add/', DutyEnlist, name='duty_enlist'),
    path('duty/<int:duty_id>/edit/', DutyEdit, name='duty_edit'),
    path('duty/<int:duty_id>/confirm_delete/', DutyDelete, name='duty_delete'),
    path('shortlist/', ShortlistList, name='shortlist_list'),
    path('shortlist/add', ShortlistEnlist, name='shortlist_enlist'),
    path('shortlist/<int:shortlist_id>/edit/', ShortlistEdit, name='shortlist_edit'),
    path('shortlist/<int:shortlist_id>/confirm_delete/', ShortlistDelete, name='shortlist_delete')
]