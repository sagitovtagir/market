from django.contrib import admin
from .models import Product, Category, ProductImage
from mptt.admin import TreeRelatedFieldListFilter
from mptt.admin import MPTTModelAdmin


# Register your models here.
@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ['name', 'is_active', 'image']
    list_filter = ['is_active']
    list_editable = ['is_active']
    search_fields = ['name', 'description']

class ProductImageInLine(admin.TabularInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['articul', 'name', 'count_product', 'is_active', 'category', 'preview']
    list_filter = ['is_active', ('category', TreeRelatedFieldListFilter)]
    list_editable = ['is_active']
    search_fields = ['name', 'category__name', 'description']
    inlines = [ProductImageInLine]





