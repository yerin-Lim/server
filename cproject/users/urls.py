from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserListView, PostViewSet

routers = DefaultRouter()
routers.register('post', PostViewSet)

urlpatterns = [
    path('', UserListView.as_view()),
    path('', include(routers.urls)),
]