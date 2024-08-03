from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from contacts.views import (
    ContactListView, 
    ContactDetailView, 
    ContactCreateView, 
    ContactUpdateView, 
    ContactDeleteView
)


urlpatterns = [
    path('contacts/create/', ContactCreateView.as_view(), name='contacts-create'),
    path('contacts/<pk>/edit/', ContactUpdateView.as_view(), name='contacts-update'),
    path('contacts/<pk>/delete/', ContactDeleteView.as_view(), name='contacts-delete'),
    # name= is a name for use in <a href=> in templates
    path('contacts/', ContactListView.as_view(), name='contacts-list'),
    path('contacts/<pk>/', ContactDetailView.as_view(), name='contacts-detail'),
]