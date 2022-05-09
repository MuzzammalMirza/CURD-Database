from django.contrib import admin
from .models import user
# Register your models here.
@admin.register(user)
class Useradmin(admin.ModelAdmin):
    list_display = ('name','email','password')
