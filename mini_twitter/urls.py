from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Mini-Twitter',
        default_version='v1'
    ),
    public=True
).with_ui('redoc', cache_timeout=0)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('openapi/', schema_view, name='openapi-schema'),

    path('api/', include('accounts.urls')),
    path('api/', include('posts.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)