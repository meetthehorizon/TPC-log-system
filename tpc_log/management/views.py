from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.cache import never_cache
from management.models import Company, Process, Duty, Shortlist
from management.forms import CompanyForm, ProcessForm, DutyForm, ShortlistForm

def permission_company(user):
    return True
def permission_process(user):
    return True
def permission_duty(user):
    return True
def permission_shortlist(user):
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

@never_cache
@login_required
@user_passes_test(permission_duty)
def DutyList(request):
    # Get the filter parameters from the request's GET data
    date_filter = request.GET.get('date')
    company_filter = request.GET.get('company')

    # Start with all duties and select related fields
    duties = Duty.objects.all().select_related('process_id__company_id', 'tpc_id')

    # Apply filters if provided
    if date_filter:
        duties = duties.filter(process_id__date=date_filter)

    if company_filter:
        duties = duties.filter(process_id__company_id=company_filter)

    # Retrieve a list of all companies for the dropdown filter
    companies = Company.objects.all()

    context = {
        'duties': duties,
        'companies': companies,
    }
    return render(request, 'duty_list.html', context)


@never_cache
@login_required
@user_passes_test(permission_duty)
def DutyEnlist(request):
    if request.method == 'POST':
        form = DutyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('duty_list')  # Redirect to the duty list page after adding a duty
    else:
        form = DutyForm()

    return render(request, 'duty_form.html', {'form': form})

@never_cache
@login_required
@user_passes_test(permission_duty)
def DutyDelete(request, duty_id):
    duty = Duty.objects.get(pk=duty_id)
    if request.method == 'POST':
        duty.delete()
        return redirect('duty_list')  # Redirect to the duty list page after deleting a duty

    return render(request, 'duty_confirm_delete.html', {'duty': duty})

@never_cache
@login_required
@user_passes_test(permission_duty)
def DutyEdit(request, duty_id):

    duty = Duty.objects.get(pk=duty_id)
    
    if request.method == 'POST':
        form = DutyForm(request.POST, instance=duty)
        if form.is_valid():
            form.save()
            return redirect('duty_list')  # Redirect to the duty list page after editing a duty
    else:
        form = DutyForm(instance=duty)

    return render(request, 'duty_edit.html', {'form': form, 'duty': duty})

@never_cache
@login_required
@user_passes_test(permission_shortlist)
def ShortlistList(request):
    students = User.objects.all()  # Get a list of all students
    companies = Company.objects.all()  # Get a list of all companies

    # Filter Shortlist records based on the provided parameters
    company_filter = request.GET.get('company')
    student_filter = request.GET.get('student')
    date_filter = request.GET.get('date')

    shortlist_query = Shortlist.objects.all()

    if company_filter:
        shortlist_query = shortlist_query.filter(process_id__company_id=company_filter)
    if student_filter:
        shortlist_query = shortlist_query.filter(student_id__roll_number=student_filter)
    if date_filter:
        shortlist_query = shortlist_query.filter(process_id__date=date_filter)

    shortlists = shortlist_query.select_related('student_id', 'process_id__company_id').order_by('-process_id__date')

    context = {
        'students': students,
        'shortlists': shortlists,
        'company_filter': company_filter,
        'student_filter': student_filter,
        'date_filter': date_filter,
        'companies': companies,
    }

    return render(request, 'shortlist_list.html', context)


@never_cache
@login_required
@user_passes_test(permission_shortlist)
def ShortlistEnlist(request):
    if request.method == 'POST':
        form = ShortlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('duty_list')  # Redirect to the duty list page after adding a duty
    else:
        form = ShortlistForm()

    return render(request, 'shortlist_form.html', {'form': form})

@never_cache
@login_required
@user_passes_test(permission_shortlist)
def ShortlistDelete(request, shortlist_id):
    shortlist = Shortlist.objects.get(pk=shortlist_id)
    if request.method == 'POST':
        shortlist.delete()
        return redirect('shortlist_list')
    
    return render(request, 'shortlist_confirm_delete.html', {'shortlist': shortlist})

@never_cache
@login_required
@user_passes_test(permission_shortlist)
def ShortlistEdit(request, shortlist_id):
    # return HttpResponse("Shortlist Edit")
    shortlist = get_object_or_404(Shortlist, pk=shortlist_id)

    if request.method == 'POST':
        form = ShortlistForm(request.POST, instance=shortlist)
        if form.is_valid():
            form.save()
            return redirect('shortlist_list')  # Redirect to the process list page after editing
    else:
        form = ShortlistForm(instance=shortlist)

    return render(request, 'shortlist_edit.html', {'form': form, 'shortlist': shortlist})

