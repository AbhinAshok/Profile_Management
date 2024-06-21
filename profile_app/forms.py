from django import forms
from .models import Profile, Project, Portfolio
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'address', 'email', 'skills', 'contact_details']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'link']

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['project', 'work_experience', 'education', 'certification']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))