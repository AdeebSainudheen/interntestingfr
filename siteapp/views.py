from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def home(request):
    return render(request, 'home.html', {
        'name': 'Your Name',
        'headline': 'Frontend Developer & Designer',
        'intro': 'I build clean, modern websites using Django, HTML, CSS, and JavaScript.',
        'projects': [
            {
                'title': 'Personal Portfolio',
                'description': 'A responsive portfolio website to showcase projects and skills.',
            },
            {
                'title': 'Landing Page',
                'description': 'A simple product landing page with smooth scrolling and animations.',
            },
            {
                'title': 'Blog Template',
                'description': 'A clean blog layout with project details and contact information.',
            },
        ],
        'skills': ['HTML', 'CSS', 'JavaScript', 'Django', 'Responsive Design'],
    })


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created successfully.')
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')
