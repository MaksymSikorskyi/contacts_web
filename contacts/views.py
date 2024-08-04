from django.forms import BaseModelForm
from django.utils.text import slugify
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
    )

from .models import Contact
from .forms import ContactForm


# functional based handler
def home(request):
    return render(request, 'index.html')


# Generic views in dgango docs views section. Class based handler
class ContactListView(ListView):
    model = Contact
    # for setting query
    queryset = Contact.objects.order_by('name')
    # important! name for use in templates
    context_object_name = 'contacts'


# another example of generic views from Django lib
class ContactDetailView(DetailView):
    model = Contact
    context_object_name = 'contact'


# class for forms
class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm

    # redefining method from parent class
    def form_valid(self, form):
        form.instance.update_slug()
        return super().form_valid(form)


class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm

     # redefining method from parent class
    def form_valid(self, form):
        form.instance.update_slug()
        return super().form_valid(form)


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts-list')
    context_object_name = 'contact'
