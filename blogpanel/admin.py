# blogpanel/admin.py
from django.contrib import admin
from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('catname',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_name', 'datetime_post')
    list_filter = ('category_name',)
    search_fields = ('title', 'content')
