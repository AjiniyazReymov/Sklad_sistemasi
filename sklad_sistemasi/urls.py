from django.contrib import admin
from django.urls import path, include

from drf_yasg.app_settings import redoc_settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Books list API",
        default_version='v1',
        description="Library demo project",
        terms_of_service="demo.com",
        contact=openapi.Contact(email="<rajiniyaz5@gmail.com>"),
        license=openapi.License(name="demo License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warehouse/', include('sklad.urls')),

    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # swagger
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'
         ),
    path('redoc', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc',
         ),
]