from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_date', 'modified_date')
    list_display_links = ('name',)

admin.site.register(Category, CategoryAdmin)
