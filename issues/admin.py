from django.contrib import admin

# Register your models here.
from .models import Category, Issue

admin.site.register(Category)
admin.site.register(Issue)