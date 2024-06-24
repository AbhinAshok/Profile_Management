from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Project
from .forms import ProfileForm, ProjectForm, PortfolioForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserLoginForm

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    projects = profile.projects.all()
    return render(request, 'profile.html', {'profile': profile, 'projects': projects})

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = request.user.profile
            project.save()
            return redirect('profile_view')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})


@login_required
def portfolio_view(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            return redirect('profile')
    else:
        form = PortfolioForm()
    return render(request, 'portfolio.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_view')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile_view')
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})