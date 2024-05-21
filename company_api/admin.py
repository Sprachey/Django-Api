from django.contrib import admin
from .models import Employee,Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','location','domain']
    search_fields = ['name']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','email','company']
    list_filter = ["company"]

# Register your models here.
admin.site.register(Employee,EmployeeAdmin,filter=Company)

admin.site.register(Company,CompanyAdmin)