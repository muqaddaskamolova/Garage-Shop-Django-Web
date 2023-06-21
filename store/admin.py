from django.contrib import admin
from .models import *


# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    # form = ProductAdminForm
    # sets values for how the admin site lists your products
    inlines = [
        ProductImageInline,
    ]
    list_display = [
        'pk', 'name', 'slug', 'price', 'old_price', 'created_at', 'updated_at', 'color', 'material',
        'status', 'quantity', 'in_stock', ]
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    list_editable = ['price', 'quantity', 'color', 'material', 'in_stock', ]
    list_filter = ['name', 'price', 'is_active', 'quantity', 'color', 'material', 'category']


search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
exclude = ('created_at', 'updated_at',)
# sets up slug to be generated from product name
prepopulated_fields = {'slug': ('name',)}
# registers your product model with the admin site
admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    # sets up values for how admin site lists categories
    list_display = ['name', 'slug', 'created_at', 'updated_at', ]
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    list_filter = ['name', 'created_at', 'updated_at']
    # sets up slug to be generated from category name
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

# def clean_price(self):
#  if self.cleaned_data['price'] <= 0:
#     raise forms.ValidationError('Price must be greater than zero.')
# return self.cleaned_data['price']
