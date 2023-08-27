from django.contrib import admin
from .models import BlogPage_2


@admin.register(BlogPage_2)
class BlogPageAdmin(admin.ModelAdmin):
    list_display = ['intro', 'date']
   #prepopulated_fields = {'slug': ('intro',)}


