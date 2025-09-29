from django.contrib import admin
from newspaper.models import (
    Advertisement, Comment, Contact, Newsletter, OurTeam, Post, Category, Tag
)
from django_summernote.admin import SummernoteModelAdmin
from unfold.admin import ModelAdmin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "icon")
    search_fields = ("name",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)

@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ("name", "position")
    search_fields = ("name", "position")

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_at")
    search_fields = ("post__title", "user__username", "content")

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
    search_fields = ("email",)

@admin.register(Post)
class PostAdmin(ModelAdmin, SummernoteModelAdmin):
    summernote_fields = ("content",)
    list_display = (
        "title", "author", "status", "category",
        "published_at", "views_count", "is_breaking_news"
    )
    list_filter = ("status", "category", "tag", "is_breaking_news")
    search_fields = ("title", "content")
    ordering = ("-published_at",)
