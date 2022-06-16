from rest_framework import serializers
from blog.models import Post, Category

class PostSerializer(serializers.ModelSerializer):
  category = serializers.StringRelatedField()
  class Meta:
    model = Post
    fields = ['id', 'title', 'author','excerpt', 'content','status','category', 'date']

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = "__all__"