# views.py

from django.shortcuts import render
from management.models import Duty, Process, Company
from users.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#@login_required
def duties_view(request):
    try:
        user = User.objects.get(roll_number = request.user.roll_number)
        user_objects = Duty.objects.filter(tpc_id=user).select_related('Process__Company__User')
        context = {
            'user_objects': user_objects
        }

        return render(request, 'duties.html', context)
    except User.DoesNotExist:
        # Handle the case where the user does not exist
        return HttpResponse("User does not exist")

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

