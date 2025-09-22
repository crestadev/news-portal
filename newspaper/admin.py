from django.contrib import admin

from newspaper.models import Advertisement, Comment, Contact, Newsletter, OurTeam, Post, Category, Tag
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Advertisement)
admin.site.register(OurTeam)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Newsletter)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)


admin.site.register(Post, PostAdmin)