"""
URL configuration for HomeHunt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    info=openapi.Info(
        title='Home Hunt Open API',
        default_version='1',
        description='''API for apartments reservation system.''',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(
            name='Oleksii Solodkov',
            email='test.email@gmail.com',
        ),
        license=openapi.License(
            name="CrazyHedgehog License"
        )
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.router')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=1000)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=1000)),
]
