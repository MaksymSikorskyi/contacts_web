from django.contrib import admin

from .models import Contact, Category


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # !!! optimisation requests on DB( n+1 request problem)
    list_select_related = ("category",)

    # prepopulated fields for admin interface
    prepopulated_fields = {
        "slug": (
            "sex",
            "name",
        )
    }

    # to show atributes of the class on admin interfase
    list_display = (
        "pk",
        "is_favorite",
        "email",
        "category",
        "full_name",
        "slug",
        "phone",
        "has_address",
        "created_at",
    )

    # to register atributes for search on admin interface
    search_fields = ("email", "name", "phone")

    # to make an edit link of class atribute on admin interface
    list_display_links = ("email", "full_name")

    # items for filtering on admin interface
    list_filter = ("sex", "created_at", "category")

    # the name of the field is selfexplainatory
    readonly_fields = ("created_at", "updated_at")

    # ordering of items displayed on admin interface
    ordering = ("name",)

    # decorator to show boolean value graphicaly
    @admin.display(boolean=True)

    # method to display result on admin interfase
    def has_address(self, obj: "Contact"):
        return obj.address is not None and len(obj.address.strip()) > 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "created_at")
    list_display_links = ("pk", "name")
    list_filter = ("created_at",)
    readonly_fields = ("created_at", "updated_at")
