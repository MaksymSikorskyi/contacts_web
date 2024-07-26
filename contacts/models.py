from django.db import models


class Contact(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True, default=None)
    notes = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "<Contact id={} email={} phone={}>".format(
            self.pk, self.email, self.name, self.phone
        )
