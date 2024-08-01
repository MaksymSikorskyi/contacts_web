"""
URL configuration for contacts_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from contacts.views import home, ContactListView, ContactDetailView, ContactCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # second slash in PATH is neccessary
    path('contacts/create/', ContactCreateView.as_view(), name='contacts-create'),
    # name= is a name for use in <a href=> in templates
    path('contacts/', ContactListView.as_view(), name='contacts-list'),
    path('contacts/<pk>/', ContactDetailView.as_view(), name='contacts-detail'),
    path('', home, name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
