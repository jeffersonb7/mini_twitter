from django.contrib import admin
from django.urls import path, include
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
    path('openapi/', schema_view, name='openapi-schema')
]