from django.urls import path
from . import views
from .views import index, ProfileView, settings, ProfileView, UserSearch, AddFollower, RemoveFollower

urlpatterns = [
    path('', index.as_view(), name='landing'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('settings/', settings.as_view(), name='settings'),
    path('search/', views.UserSearch, name='search'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
]