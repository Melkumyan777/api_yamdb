from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import get_token, UserRegistrationViewSet, DummyViewSet

v1_router = DefaultRouter()
v1_router.register('auth/signup', UserRegistrationViewSet, basename='signup')
v1_router.register('users', DummyViewSet, basename='users')
v1_router.register('titles', DummyViewSet, basename='titles')
v1_router.register('categories', DummyViewSet, basename='categories')
v1_router.register('genres', DummyViewSet, basename='genres')
v1_router.register('reviews', DummyViewSet, basename='reviews')
v1_router.register('comments', DummyViewSet, basename='comments')

urlpatterns = [
    path('auth/token/', get_token, name='get_token'),
    path('', include(v1_router.urls)),
]
