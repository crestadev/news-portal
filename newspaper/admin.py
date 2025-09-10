from django.contrib import admin

from newspaper.models import Post, Category, Tag

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
