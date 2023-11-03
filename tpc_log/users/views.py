# views.py
from tpc_log.settings import AUTH_USER_MODEL
from django.shortcuts import render, redirect, HttpResponse
from .forms import SignUpForm, StudentLoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Additional custom logic after successful registration
            return redirect(reverse('student-login'))# Redirect to the login page

    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                is_tpr = request.user.groups.filter(name='TPR').exists()
                context ={ 'user': user,
                          'is_tpr': is_tpr}
                # Redirect to a success page or any other desired page
                return render(request,'dashboard.html', context)
            else:
                return HttpResponse("user dne")
    else:
        form = StudentLoginForm()

    return render(request, 'student-login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect("/")  # Change 'home' to the URL name you want to use

def home(request):
    return render(request, 'home.html')