from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Project

def home(request):

    name = "Prabhakar Yadav"
    photo_url = "https://avatars3.githubusercontent.com/Prabhu13"
    email = "py98@njit.edu"
    github_link = "https://github.com/Prabhu13"

    context = {
        'name': name,
        'photo_url': photo_url,
        'email': email,
        'github_link': github_link,
    }

    return render(request, 'portfolio/home.html', context)

def portfolio(request):
    # Retrieve the project details from the model
    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'portfolio/portfolio.html', context)

def about(request):
    # Define information about yourself
    about_text = "I am a web developer with a passion for coding."

    context = {
        'about_text': about_text,
    }

    return render(request, 'portfolio/about.html', context)
