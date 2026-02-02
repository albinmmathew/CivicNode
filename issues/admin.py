from django.contrib import admin

# Register your models here.
from .models import Category, Issue, Upvote

admin.site.register(Category)
admin.site.register(Issue)
admin.site.register(Upvote)
