from django.contrib import admin

# Register your models here.
from .models import Employee, Device

admin.site.register(Employee)
admin.site.register(Device)
