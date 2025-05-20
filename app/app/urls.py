"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app.views import GameViewSet, PlatformViewSet, StudioViewSet

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r"games", GameViewSet, basename="games")
router.register(r"studios", StudioViewSet, basename="studios")
router.register(r"platforms", PlatformViewSet, basename="platforms")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
] + debug_toolbar_urls()
