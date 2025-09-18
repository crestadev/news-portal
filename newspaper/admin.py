from django.contrib import admin

from newspaper.models import Advertisement, Comment, Contact, OurTeam, Post, Category, Tag

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Advertisement)
admin.site.register(OurTeam)
admin.site.register(Contact)
admin.site.register(Comment)