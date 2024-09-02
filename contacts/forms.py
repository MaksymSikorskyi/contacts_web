from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            "category",
            "is_favorite",
            "sex",
            "name",
            "photo",
            "email",
            "phone",
            "address",
            "notes",
        )
        # standart widgets customization
        widgets = {
            "address": forms.Textarea(attrs={"rows": 2}),
            "notes": forms.Textarea(attrs={"rows": 2}),
        }
