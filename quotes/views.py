"""Quotes views"""
import json
from django.views.generic import ListView
from .models import Quote

# Create your views here.
class HomeView(ListView):
    """Home page view"""
    model = Quote
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        """Pass quotes as json objects to context"""
        context = super().get_context_data(**kwargs)
        quotes_list = []
        for quote in Quote.objects.all():
            new_quote = {
                'id': quote.id,
                'text': quote.text,
                'movie': quote.movie,
                'quote_len': quote.quote_len
            }
            quotes_list.append(new_quote)
        context["quotes_list"] = json.dumps(quotes_list)
        return context
   