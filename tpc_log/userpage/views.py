# views.py

from django.shortcuts import render
from management.models import Duty
from users.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# @login_required
# def duties_view(request):
#     try:
#         user = User.objects.get(roll_number = request.user.roll_number)
#         user_objects = Duty.objects.filter(tpc_id=user).select_related('process_id', 'company_id', 'spoc_id')
#         context = {
#             'user_objects': user_objects
#         }

#         return render(request, 'duties.html', context)
#     except User.DoesNotExist:
#         # Handle the case where the user does not exist
#         return HttpResponse("User does not exist")
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
    name=request.user.name
    # return HttpResponse("hey")

# @login_required
# def dutiesview(request):
#     user_id= request.user.roll_number
#     tpr = User.objects.filter(tpc_id = user_id)
#     duties = Duty.objects.filter(tpc_id = user_id)
#     processes = Process.objects.filter(process_id = duties.process_id)
#     companies = Company.objects.filter(company_id = processes.company_id)
#     spoc = User.objects.filter(roll_number=processes.spoc_id)
#     context ={
#         'duties': duties,
#         'processes': processes,
#         'companies': companies,
#         'spoc': spoc,
#     }
#     return render(request, 'duties.html', context)

@never_cache
@login_required
def duties_view(request):
    user_id = request.user.roll_number
    duties = Duty.objects.filter(tpc_id=user_id).select_related('process_id__company_id', 'process_id__spoc_id')
    if not duties.exists():
        return HttpResponse("No duties found for this user", status=404)
    else:
        return render(request, 'duties.html', {'duties': duties})

        
    
    context = {
        'duties': duties,
    }
    return render(request, 'duties.html', context)