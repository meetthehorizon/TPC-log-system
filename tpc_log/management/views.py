from django.shortcuts import render
from users.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.cache import never_cache
from management.models import Company

# Create your views here.
@never_cache
@login_required
@user_passes_test(lambda user: user.role == 'STUDENT')
def company_list(request):
    
    companies = Company.objects.all()
    context = {
        'companies': companies,
    }

    return render(request, 'company_list.html', context)
    