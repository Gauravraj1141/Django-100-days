from django.contrib import admin
from .models import students
# Register your models here


@admin.register(students)
class studentsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'roll', 'Address', )
