from django.contrib import admin

from .models import Blog, Category, Comment


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ( 'id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)

# Register your models here.

admin.site.register(Category)  # Register your About model here
admin.site.register(Blog, BlogAdmin)  # Register your Blog model here

admin.site.register(Comment)