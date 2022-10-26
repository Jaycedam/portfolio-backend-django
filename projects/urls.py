from django.urls import path, include
from .views import ProjectViewSet, AreaViewSet
from rest_framework import routers

# routes for the viewsets API
router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('areas', AreaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]