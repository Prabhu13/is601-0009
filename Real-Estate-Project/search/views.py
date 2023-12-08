from django.views.generic import ListView
from listing.models import Property
# Create your views here.



class SearchView(ListView):
    model = Property 
    template_name = "site/search.html"
    context_object_name = 'listings'
    paginate_by = 20
    
    def get_queryset(self):
        # Start with an empty queryset
        queryset = Property.objects.all()

        # Keywords
        keywords = self.request.GET.get('keywords', '')
        if keywords:
            queryset = queryset.filter(description__icontains=keywords)

        # City
        city = self.request.GET.get('city', '')
        if city:
            queryset = queryset.filter(city__iexact=city)

        # State
        state = self.request.GET.get('state', '')
        if state:
            queryset = queryset.filter(state__iexact=state)

        # Bedrooms
        bedrooms = self.request.GET.get('bedrooms', '')
        if bedrooms:
            queryset = queryset.filter(bedrooms__iexact=bedrooms)

        # Price
        price = self.request.GET.get('price', '')
        if price:
            queryset = queryset.filter(price__lte=price)

        return queryset