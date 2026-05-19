from django.shortcuts import render


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
