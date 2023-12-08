from django.urls import path
from . import views
from .views import login_view, logout_view, project_form_view


app_name = 'portfolio'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', views.home, name='home'),
    # path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('about/', views.about, name='about'),
    path('add_project/', project_form_view, name='add_project')
]