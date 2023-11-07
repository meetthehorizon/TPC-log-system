from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from tpc_log.settings import AUTH_USER_MODEL
from .models import User
from django import forms
	
class SignUpForm(UserCreationForm):
    class Meta:
             model = User
             fields =['name', 'email', 'branch', 'degree', 'roll_number','phone_number']
	      

class StudentLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
            