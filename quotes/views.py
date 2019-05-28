"""Quotes views"""
from django.views.generic import ListView
from .models import Quote

# Create your views here.
class HomeView(ListView):
    """Home page view"""
    model = Quote
    template_name = "index.html"
