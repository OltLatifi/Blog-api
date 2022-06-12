from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions, BasePermission, SAFE_METHODS

class PostUserWritePermission(BasePermission):
  message="Editing post is restricted to the author only."
  # allows anyone to access as long as the request is get, options, head
  # so if you dont own a post you can't modify it in any way.
  def has_object_permission(self, request, view, obj):
    if request.method in SAFE_METHODS: #(GET, HEAD, OPTIONS)
      return True
    # check is it's the user who is the owner.
    return obj.author == request.user

class PostList(generics.ListCreateAPIView):
  permission_classes=[DjangoModelPermissions]
  queryset = Post.postobjects.all() #custom objects
  serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
  permission_classes=[PostUserWritePermission]

  queryset = Post.objects.all() #custom objects
  serializer_class = PostSerializer