from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)

    city = models.CharField(max_length=100, blank=True, null=True)

    service_type = models.CharField(
        max_length=100,
        choices=[
            ('home', 'Home Solar'),
            ('business', 'Business Solar'),
            ('industrial', 'Industrial Solar'),
            ('lighting', 'Solar Lighting'),
            ('maintenance', 'Maintenance'),
            ('other', 'Other'),
        ],
        blank=True,

    )

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name