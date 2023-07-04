from django import forms
from .models import Tasks
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class addTaskForm(forms.ModelForm):
    title = forms.CharField(max_length=209, label="Enter the title:", widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(label="Enter the due date:", widget=DateInput(attrs={'class': 'form-control'}))
    time = forms.TimeField(label="Enter the due time:", widget=TimeInput(attrs={'class': 'form-control'}))

    
    class Meta:
        model = Tasks
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=200, label="Enter a username", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a username'}))
    email = forms.EmailField( widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    password1 = forms.CharField(label="Enter a password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter a password'}))
    password2 = forms.CharField( label="Confirm password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']