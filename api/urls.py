from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r"tags", views.TagViewSet)
router.register(r"categories", views.CategoryViewSet)
router.register(r"posts", views.PostViewSet)
router.register[r"posts", views.PostViewSet]

urlpatterns = [
    path('', include(router.urls)),
    path("post-by-category/<int:category_id>/",views.PostListByCategoryView.as_view(),name="post-list-by-category-api"),
    path("post-by-tag/<int:tag_id>/",views.PostListByTagView.as_view(),name="post-list-by-tag-api"),
    path("draft-list/", views.DraftListView.as_view(), name="draft-list-api"),
    path("draft-detail/", views.DraftDetailView.as_view(), name="draft-detail-api"),
    path("post-publish/", views.PostPublishViewSet.as_view(), name="post-pubish-api"),
    path("post/<int:post_id>/comments/", views.CommentListCreateAPIView.as_view(), name="comment-list-create-api"),
    path("post/<int:post_id>/comments/<int:pk>/", views.CommentDetailAPIView.as_view(), name="comment-detail-api"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]