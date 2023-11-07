from django.shortcuts import render
from django.http import HttpResponse
from management.models import Company, Shortlist, Process
from users.models import User
from .forms import RoundForm
from .models import Round

def logview(request, process_id):
    students = Shortlist.objects.filter(process_id= process_id)
    form = RoundForm()
    company_name = Process.objects.get(process_id=process_id).company_id.company_name
    return render(request, "logsheet.html", {"students": students, "form": form, 'company_name': company_name })
