from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import get_token, UserRegistrationViewSet

v1_router = DefaultRouter()
v1_router.register('auth/signup', UserRegistrationViewSet, basename='signup')


urlpatterns = [
    path('auth/token/', get_token, name='get_token'),
    path('', include(v1_router.urls)),
]
