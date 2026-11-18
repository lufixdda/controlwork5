from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

post_comments_router = DefaultRouter()
post_comments_router.register(r'comments', CommentViewSet, basename='post-comment')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_pk>/', include((post_comments_router.urls, 'post_comments'), namespace='post-comments')),
]