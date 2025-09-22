from django.contrib import admin

from newspaper.models import Advertisement, Comment, Contact, Newsletter, OurTeam, Post, Category, Tag
from django_summernote.admin import SummernoteModelAdmin
from unfold.admin import ModelAdmin

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Advertisement)
admin.site.register(OurTeam)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Newsletter)





admin.register(Post)
class CustomAdminClass(ModelAdmin, SummernoteModelAdmin):
    summernote_fields = ("content",)

    class Meta:
        model = Post