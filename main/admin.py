from django.contrib import admin

from .models import Main,Contact
# Register your models here.

admin.register(Main,Contact)(admin.ModelAdmin)
