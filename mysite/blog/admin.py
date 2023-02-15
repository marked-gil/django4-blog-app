from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ sets the model fields that gets displayed on the admin object list page """
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    """ specifies the model fields to filter results by """
    list_filter = ['status', 'created', 'publish', 'author']
    """ creates a search bar & defines a list of searchable fields """
    search_fields = ['title', 'body']
    """ prepopulates the slug field with the title field"""
    prepopulated_fields = {'slug': ('title',)}
    """ displays a lookup widget on the author field """
    raw_id_fields = ['author']
    """ creates a navigation links to navigate through a date hierarchy """
    date_hierarchy = 'publish'
    """ specifies the default sorting criteria"""
    ordering = ['status', 'publish']