from django.urls import path, include
from .views import ProjectViewSet, AreaViewSet
from rest_framework import routers

# JWT Authentication Views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# routes for the viewsets API
router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('areas', AreaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]