from rest_framework.schemas import get_schema_view
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static

# from blog_api.views import LikeListApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('api/user/', include('users.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls', namespace="rest_framework")),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/', include('blog_api.urls', namespace='blog_api')),
    path('docs/', include_docs_urls(title="BlogAPI")),
    path('schema', get_schema_view(
        title='BlogAPI',
        description='API for a blog',
        version='1.0.0',
    ), name="openapi-schema"),
    # path('likes/<str:slug>', LikeListApiView.as_view())
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)