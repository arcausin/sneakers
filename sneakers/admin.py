from django.contrib import admin

from .models import Produit

# Register your models here.

class ProduitAdmin(admin.ModelAdmin):
    fields =['name', 'image', 'description', 'quantity']

admin.site.register(Produit)