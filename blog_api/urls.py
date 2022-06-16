from rest_framework.routers import DefaultRouter
from .views import PostList, CategoryList, CreatePost, AdminDetail, EditPost, DeletePost
from django.urls import path

app_name = 'blog_api'

router = DefaultRouter()
router.register('', PostList, basename="post")

urlpatterns = [
  path('categories/', CategoryList.as_view(), name='categories'),
  # Post Admin URLs
  path('create/', CreatePost.as_view(), name='createpost'),
  path('edit/postdetail/', AdminDetail.as_view(), name='admindetailpost'),
  path('edit/<int:pk>/', EditPost.as_view(), name='editpost'),
  path('delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]
urlpatterns += router.urls