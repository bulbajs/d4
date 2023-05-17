from django.contrib import admin

# Register your models here.
from .models import Post, PostCategory, Category


admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Category)