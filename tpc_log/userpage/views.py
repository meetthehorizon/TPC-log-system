# views.py

from django.shortcuts import render
from management.models import Duty, Shortlist
from users.models import User
from management.models import Company
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def userinfo(request):
    try:
        user_id=request.user.roll_number
        user = User.objects.get(roll_number=user_id)
    except User.DoesNotExist:
        # Handle the case where the object with the given ID doesn't exist
        return HttpResponse("user does not exist")

    return render(request, 'userinfo.html', {'user': user})


@never_cache
@login_required
def duties_view(request):
    user_id = request.user.roll_number
    duties = Duty.objects.filter(tpc_id=user_id).select_related('process_id__company_id', 'process_id__spoc_id')
    if not duties.exists():
        return HttpResponse("No duties found for this user", status=404)
    else:
        return render(request, 'duties.html', {'duties': duties})

@login_required
def preference_list(request):
    company_list = Company.objects.all()

@login_required
def shortlist(request):
    student_id= request.user.roll_number
    processes = Shortlist.objects.filter(student_id=student_id).select_related("process_id")
    return render(request, 'shortlist.html',{'processes': processes} )