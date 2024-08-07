from tabnanny import verbose
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class SexOption(models.TextChoices):
    MAN = 'man', _('Man')
    WOMAN = 'woman', _('Woman')
    OTHER = 'other', _('Other')


class Contact(models.Model):
    slug = models.SlugField(unique=True, max_length=150, null=True, blank=False)
    sex = models.CharField(verbose_name=_('sex'), max_length=10, default=SexOption.MAN, choices=SexOption.choices)
    email = models.EmailField(verbose_name=_('email'), unique=True)
    name = models.CharField(verbose_name=_('name'), max_length=150)
    phone = models.CharField(verbose_name=_('phone'), max_length=15)
    address = models.TextField(verbose_name=_('address'), blank=True, null=True, default=None)
    notes = models.TextField(verbose_name=_('notes'), blank=True, null=True, default=None)
    photo = models.ImageField(verbose_name=_('photo'), blank=True, null=True, upload_to='%Y/%m')
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated at'), auto_now=True)

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')

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
    
    # can be replased by AutoSlugField from django extensions package
    def update_slug(self):
        self.slug = slugify('-'.join([self.sex, self.name]))
    
    # IMPORTANT. This method helps generate url
    def get_absolute_url(self):
        return reverse("contacts-detail", kwargs={"slug": self.slug})
    
