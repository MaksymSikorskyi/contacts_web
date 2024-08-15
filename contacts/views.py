from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
    )

from .models import Contact, Category
from .forms import ContactForm


# functional based handler
def home(request):
    return render(request, 'index.html')


# Generic views in dgango docs views section. Class based handler
class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    # for setting query. 
    # !!! important, .select_related() is a method for decreasing requests on DB
    queryset = Contact.objects.order_by('name').select_related('category')
    
    # important! name for use in templates
    context_object_name = 'contacts'

    # !!! revriting legacy method for filtration
    def get_queryset(self):
        qs = super().get_queryset()

        # additional filtration
        category_id = self.request.GET.get('category')
        if category_id:
            qs = qs.filter(category_id=category_id)
        return qs
    
    # !!!  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_id = self.request.GET.get('category')

        context['category'] = None

        if category_id:
            context['category'] = Category.objects.get(pk=category_id)

        return context


# another example of generic views from Django lib
class ContactDetailView(LoginRequiredMixin, DetailView):
    model = Contact
    context_object_name = 'contact'


# class for forms
class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactForm

    # redefining method from parent class
    def form_valid(self, form):
        form.instance.update_slug()
        return super().form_valid(form)


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    form_class = ContactForm

    # redefining method from parent class
    def form_valid(self, form):
        form.instance.update_slug()
        return super().form_valid(form)


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts-list')
    context_object_name = 'contact'
