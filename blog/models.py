from django.db import models
from django.conf import settings

class Category(models.Model):
  name = models.CharField(max_length=255)
  def __str__(self):
    return self.name

class Post(models.Model):

  class PostObjects(models.Manager):
    def get_queryset(self):
      return super().get_queryset().filter(status='published')
  # returns only the published posts

  options=(
    ('draft','Draft'),
    ('published','Published'),
  )
  category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
  title = models.CharField(max_length=255)
  excerpt = models.TextField(null=True)
  content = models.TextField()
  slug = models.SlugField(max_length=255, unique_for_date='published')
  published = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'blog_posts')
  status = models.CharField(max_length=10, choices=options, default='published')
  date = models.DateTimeField(auto_now_add=True)

  objects = models.Manager() # default manager (no need to write this)
  postobjects = PostObjects() # custom manager for only published data

  class Meta:
    ordering = ('-published',)
  
  def __str__(self):
    return self.title