from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ sets the model fields that gets displayed on the admin object list page """
    list_display = ['title', 'slug', 'author', 'publish', 'status']