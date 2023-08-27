from django.contrib import admin
from .models import Category, Product, CrewCategoryItem


class CrewCategoryItemInline(admin.TabularInline):
    model = CrewCategoryItem
    raw_id_fields = ['user']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CrewCategoryItemInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'serices_types', 'price',
                    'available', 'name', 'updated']
    list_filter = ['available', 'serices_types', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}



