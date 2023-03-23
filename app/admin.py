from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class UserAdminregister(admin.ModelAdmin):
    list_display=['contact','email','password']