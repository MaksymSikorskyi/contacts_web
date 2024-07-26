from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    # to show atributes of the class on admin interfase
    list_display = ('pk', 'email', 'name', 'phone', 'has_address')

    # to register atributes for search on admin interface
    search_fields = ('email', 'name', 'phone')

    # to make an edit link of class atribute on admin interface
    list_display_links = ('email', 'name')

    # ordering of items displayed in admin interface
    ordering = ('name',)

    # decorator to show boolean value graphicaly
    @admin.display(boolean=True)
    # method to display result on admin interfase
    def has_address(self, obj: 'Contact'):
        return obj.address is not None and len(obj.address.strip()) > 0