from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'username']
    # ordering = ['order_number']


admin.site.register(CustomUser, CustomUserAdmin)
