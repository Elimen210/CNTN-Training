from django.urls import path
from . import views
from .views import index, ProfileView, settings, ProfileView

urlpatterns = [
    path('', index.as_view(), name='landing'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('settings/', settings.as_view(), name='settings'),
]