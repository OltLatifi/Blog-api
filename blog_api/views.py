from django.shortcuts import get_object_or_404
from blog.models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters import rest_framework as filters
from rest_framework.parsers import MultiPartParser, FormParser
class PostUserWritePermission(BasePermission):
  message="Editing post is restricted to the author only."
  # allows anyone to access as long as the request is get, options, head
  # so if you dont own a post you can't modify it in any way.
  def has_object_permission(self, request, view, obj):
    if request.method in SAFE_METHODS: #(GET, HEAD, OPTIONS)
      return True
    # check is it's the user who is the owner.
    return obj.author == request.user

class PostList(viewsets.ModelViewSet):
  permission_classes = [PostUserWritePermission]
  serializer_class = PostSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  filterset_fields = ('title','category')

  queryset = Post.postobjects.all()


  def get_object(self, queryset=None, **kwargs):
    item = self.kwargs.get('pk')
    return get_object_or_404(Post, slug=item)



# class PostList(viewsets.ViewSet):
#   permission_classes = [IsAuthenticated]
#   queryset = Post.postobjects.all()

#   def list(self, request):
#     serializer = PostSerializer(self.queryset, many=True)
#     return Response(serializer.data)

#   def retrieve(self, request, pk=None):
#     post = get_object_or_404(self.queryset, pk=pk)
#     serializer = PostSerializer(post)
#     return Response(serializer.data)


class CategoryList(generics.ListCreateAPIView):
  # permission_classes=[DjangoModelPermissions]
  queryset = Category.objects.all() #custom objects
  serializer_class = CategorySerializer


class CreatePost(APIView):
  permission_classes = [IsAuthenticated]
  parser_classes=[MultiPartParser, FormParser]
  def post(self, request, format=None):
    print(request.data)
    serializer = PostSerializer(data=request.data)
    if(serializer.is_valid()):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminDetail(generics.ListAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = PostSerializer
  def get_queryset(self):
    queryset = Post.objects.filter(author=self.request.user)
    return queryset

class EditPost(generics.RetrieveUpdateAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = PostSerializer
  queryset = Post.objects.all()
  lookup_field = "slug"

class DeletePost(generics.RetrieveDestroyAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = PostSerializer
  queryset = Post.objects.all()
  lookup_field = "slug"
