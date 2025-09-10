from django.utils import timezone
from datetime import timedelta

from django.shortcuts import render
from django.views.generic import TemplateView

from newspaper.models import Post

# Create your views here.
class HomePageView(TemplateView):
    template_name = "newsportal/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_post"] = (
            Post.objects.filter(published_at__isnull=False, status="active")
            .order_by("-published_at", "-views_count")
            .first()
        ) 

        context["popular_posts"] = Post.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-published_at")[:5]

        one_week_ago = timezone.now() - timedelta(days=7)
        context["weekly_top_posts"] = Post.objects.filter(
            published_at__isnull=False, status="active", published_at__gte = one_week_ago
        ).order_by("-published_at", "-views_count")[:5]

        context["breaking_news"] = Post.objects.filter(
            published_at__isnull=False, status="active", is_breaking_news=True
        ).order_by("-published_at")[:3]


        return context
    