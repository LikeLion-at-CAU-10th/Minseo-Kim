from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Url)

class Url(admin.TabularInline):
    model = Url

class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        Url,
    ]

admin.site.register(Profile, ProfileAdmin)