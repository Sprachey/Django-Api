from django.contrib import admin
from .models import Cafe

class CafeAdmin(admin.ModelAdmin):
    list_display = ['name','location','coffee_price']

# Register your models here.
admin.site.register(Cafe,CafeAdmin)