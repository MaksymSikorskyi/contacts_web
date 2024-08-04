from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class SexOption(models.TextChoices):
    MAN = 'man', 'Man'
    WOMAN = 'woman', 'Woman'
    OTHER = 'other', 'Other'


class Contact(models.Model):
    slug = models.SlugField(unique=True, max_length=150, null=True, blank=False)
    sex = models.CharField(max_length=10, default=SexOption.MAN, choices=SexOption.choices)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True, default=None)
    notes = models.TextField(blank=True, null=True, default=None)
    photo = models.ImageField(blank=True, null=True, upload_to='%Y/%m')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "<Contact id={} email={} phone={}>".format(
            self.pk, self.email, self.name, self.phone
        )
    
    @property
    def full_name(self):
        prefix = 'Mr.'
        if self.sex == SexOption.WOMAN:
            prefix = 'Ms.'
        elif self.sex == SexOption.OTHER:
            prefix = ''

        return f'{prefix} {self.name}'
    
    def update_slug(self):
        self.slug = slugify('-'.join([self.sex, self.name]))
    
    # IMPORTANT. This method helps generate url
    def get_absolute_url(self):
        return reverse("contacts-detail", kwargs={"slug": self.slug})
    
