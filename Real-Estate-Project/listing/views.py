from django.shortcuts import render
from django.urls import reverse_lazy
from contact.views import ContactView
from django.views.generic import CreateView , DetailView, ListView  , TemplateView 
from django.shortcuts import render, redirect
from .forms import PropertyForm
from .models import Property
from .forms import PropertyForm 

from .models import *

class HomeView(ListView):
    model = Property
    template_name = 'site/index.html'
    context_object_name = 'listings'

    def get_queryset(self):
        return self.model.objects.order_by('-list_date').filter(is_published=True)[:3]

class PropertyListView(ListView):
    model = Property
    template_name= 'site/listings.html'
    context_object_name = 'listings'
    paginate_by = 10

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'site/listing.html'
    context_object_name = 'property'
    pk_url_kwarg = 'id'


class AboutView(TemplateView):
    template_name = 'site/about.html'

    def get_context_data(self, **kwargs):
         context = super(AboutView, self).get_context_data(**kwargs)
         context['realtors'] = Realtor.objects.all()
         context['MVP'] = MVP.objects.last()
         return context

    

class PropertyCreateView(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'site/listing_form.html'  # Replace with your form template
    success_url = reverse_lazy('listing:listings')  # Redirect to listings after successful form submission

    def form_valid(self, form):
        # Set the user as the realtor when creating a new listing
        form.instance.realtor = self.request.user.realtor
        return super().form_valid(form)
    
from django.shortcuts import render, redirect
from .forms import PropertyForm

def add_listing(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success URL
    else:
        form = PropertyForm()

    # Render the form without error messages
    return render(request, 'site/listing_form.html', {'form': form})



def add_contact(request):
    if request.method == 'POST':
        form = ContactView(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success URL
    else:
        form = PropertyForm()

    return render(request, 'site/listing_form.html', {'form': form})

    