from django.shortcuts import render
from django.views.generic import ListView

from .models import Contact

# Create your views here.
def home(request):
    return render(request, 'index.html')


# Generic views in dgango docs views section
class ContactListView(ListView):
    model = Contact
    # for setting query
    queryset = Contact.objects.order_by('name')
    # important! name for use in templates
    context_object_name = 'contacts'