from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.cache import never_cache
from management.models import Company
from management.forms import CompanyForm

# Create your views here.
@never_cache
@login_required
@user_passes_test(lambda user: user.role != '')
def CompanyList(request):
    companies = Company.objects.all()
    context = {
        'companies': companies,
    }

    return render(request, 'company_list.html', context)
    
def CompanyEnlist(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            # Process the form data and save it to the database, for example
            # Redirect to a success page or return a success message
            form.save()
            return redirect('company_list')  # Change 'success_page' to the actual name of your success page URL
    else:
        form = CompanyForm()
    return render(request, 'company_form.html', {'form' : form})

def CompanyDelete(request, company_id):

    company = get_object_or_404(Company, company_id=company_id)

    if request.method == 'POST':
        # If the confirmation form is submitted with POST, delete the company and redirect to the company list page
        company.delete()
        return redirect('company_list')

    return render(request, 'company_confirm_delete.html', {'company': company})

def CompanyEdit(request, company_id):
    company = get_object_or_404(Company, company_id=company_id)

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')  # Redirect to the company list page
    else:
        form = CompanyForm(instance=company)

    return render(request, 'company_edit.html', {'form': form, 'company': company})