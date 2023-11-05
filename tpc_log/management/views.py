from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.cache import never_cache
from management.models import Company, Process
from management.forms import CompanyForm, ProcessForm

def permission_company(user):
    return True
def permission_process(user):
    return True

# Create your views here.
@never_cache
@login_required
@user_passes_test(permission_company)
def CompanyList(request):
    companies = Company.objects.all()
    context = {
        'companies': companies,
    }

    return render(request, 'company_list.html', context)

@never_cache
@login_required
@user_passes_test(permission_company)
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

@never_cache
@login_required
@user_passes_test(permission_company)
def CompanyDelete(request, company_id):

    company = get_object_or_404(Company, company_id=company_id)

    if request.method == 'POST':
        # If the confirmation form is submitted with POST, delete the company and redirect to the company list page
        company.delete()
        return redirect('company_list')

    return render(request, 'company_confirm_delete.html', {'company': company})

@never_cache
@login_required
@user_passes_test(permission_company)
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

@never_cache
@login_required
@user_passes_test(permission_process)
def ProcessList(request):
    # return HttpResponse("Process List")
    process = Process.objects.all()
    context = {
        'processes': process,
    }

    return render(request, 'process_list.html', context)

@never_cache
@login_required
@user_passes_test(permission_process)
def ProcessEnlist(request):
    if request.method == 'POST':
        form = ProcessForm(request.POST)
        if form.is_valid():
            # Process the form data and save it to the database, for example
            # Redirect to a success page or return a success message
            form.save()
            return redirect('process_list')  # Change 'success_page' to the actual name of your success page URL
    else:
        form = ProcessForm()
    return render(request, 'process_form.html', {'form' : form})

@never_cache
@login_required
@user_passes_test(permission_process)
def ProcessDelete(request, process_id):
    process = get_object_or_404(Process, pk=process_id)

    if request.method == 'POST':
        process.delete()
        return redirect('process_list')  # Redirect to the process list page after deletion

    return render(request, 'process_confirm_delete.html', {'process': process})

@never_cache
@login_required
@user_passes_test(permission_process)
def ProcessEdit(request, process_id):
    process = get_object_or_404(Process, pk=process_id)

    if request.method == 'POST':
        form = ProcessForm(request.POST, instance=process)
        if form.is_valid():
            form.save()
            return redirect('process_list')  # Redirect to the process list page after editing
    else:
        form = ProcessForm(instance=process)

    return render(request, 'process_edit.html', {'form': form, 'process': process})