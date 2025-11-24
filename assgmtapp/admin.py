from django.contrib import admin
from .models import crud

# Register your models here.


@admin.register(crud)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name',)