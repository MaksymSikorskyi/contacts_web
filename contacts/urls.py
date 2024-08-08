from django.urls import path

from contacts.views import (
    ContactListView, 
    ContactDetailView, 
    ContactCreateView, 
    ContactUpdateView, 
    ContactDeleteView
)

# <app_name>:<url_name from PATH>
app_name = 'contacts'

urlpatterns = [
    # second slash in PATH is neccessary
    path('create/', ContactCreateView.as_view(), name='create'),
    path('<slug>/edit/', ContactUpdateView.as_view(), name='update'),
    path('<slug>/delete/', ContactDeleteView.as_view(), name='delete'),
    path('<slug>/', ContactDetailView.as_view(), name='detail'),
    # name= is a name for use in <a href=> in templates
    path('', ContactListView.as_view(), name='list'),    
]