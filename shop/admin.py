from django.contrib import admin
from .models import *


class catadmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(catgry, catadmin)


class prodadmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'price', 'stock', 'img']
    list_editable = ['desc', 'price', 'stock', 'img']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(products, prodadmin)

# Register your models here.
