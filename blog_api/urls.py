from rest_framework.routers import DefaultRouter
from .views import PostList, CategoryList
from django.urls import path

app_name = 'blog_api'

router = DefaultRouter()
router.register('', PostList, basename="post")

urlpatterns = [
  path('categories/', CategoryList.as_view(), name='categories'),
]
urlpatterns += router.urls