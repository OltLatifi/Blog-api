from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
  queryset = Post.postobjects.all() #custom objects
  serializer_class = PostSerializer

class PostDetail(generics.RetrieveDestroyAPIView):
  queryset = Post.objects.all() #custom objects
  serializer_class = PostSerializer