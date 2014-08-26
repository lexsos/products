from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Shop, Product, Cost


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('title', 'weight', 'enabled')


class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'weight', 'enabled')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'enabled')


class CostAdmin(admin.ModelAdmin):
    list_display = ('product', 'shop', 'price')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cost, CostAdmin)
