from rest_framework import serializers
from blog.models import Post, Category

class PostSerializer(serializers.ModelSerializer):
  # this was necessary for the filtering to work
  category_ = serializers.StringRelatedField()
  class Meta:
    model = Post
    fields = ['id', 'title','image', 'author','excerpt', 'content','status','category_','category', 'published', 'slug']

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = "__all__"