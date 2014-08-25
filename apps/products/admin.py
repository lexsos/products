from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category


class CategoryAdmin(MPTTModelAdmin):
    list_filter = ('parent', )


admin.site.register(Category, CategoryAdmin)
