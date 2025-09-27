from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r"tags", views.TagViewSet)
router.register(r"categories", views.CategoryViewSet)
router.register(r"posts", views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path("post-by-category/<int:category_id>/",views.PostListByCategoryView.as_view(),name="post-list-by-category-api"),
    path("post-by-tag/<int:tag_id>/",views.PostListByTagView.as_view(),name="post-list-by-tag-api"),
    path("draft-list/", views.DraftListView.as_view(), name="draft-list-api"),
    path("draft-detail/", views.DraftDetailView.as_view(), name="draft-detail-api"),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]