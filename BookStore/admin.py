from django.contrib import admin
from .models import Book
# Register your models here.
@admin.register(Book)
class AdminProduct(admin.ModelAdmin):
    list_display = ('title','category')