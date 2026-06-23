from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'city', 'service_type', 'created_at')
    list_filter = ('service_type', 'city', 'created_at')
    search_fields = ('name', 'email', 'phone', 'city')
    ordering = ('-created_at',)