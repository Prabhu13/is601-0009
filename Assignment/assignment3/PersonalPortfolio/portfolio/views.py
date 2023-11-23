# Create your views here.
from django.shortcuts import render, redirect
from .models import Project
from django.views import View
from .forms import ProjectForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


@login_required(login_url='portfolio:login')
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

@login_required(login_url='portfolio:login')
def portfolio(request):
    # Retrieve the project details from the model
    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'portfolio/portfolio.html', context)

@login_required(login_url='portfolio:login')
def about(request):
    # Define information about yourself
    about_text = "I am a web developer with a passion for coding."

    context = {
        'about_text': about_text,
    }

    return render(request, 'portfolio/about.html', context)


@login_required(login_url='portfolio:login')
def project_form_view(request):
    template_name = 'portfolio/project_form.html'

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # Set the user in the form's instance before saving
            form.instance.user = request.user
            form.save()
            return redirect('portfolio:portfolio')  # Redirect to the portfolio view
    else:
        form = ProjectForm()

    return render(request, template_name, {'form': form})
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('portfolio:portfolio')
            else:
                form.add_error(None, 'Invalid login credentials')
    else:
        form = AuthenticationForm()

    return render(request, 'portfolio/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('portfolio:login')