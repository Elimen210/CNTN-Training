from django.urls import path
from . import views
from .views import index, ProfileView, settings, ProfileView, UserSearch, AddFollower, RemoveFollower, AddLike, FollowingPage, CommentPage, AddCommentLike

urlpatterns = [
    path('', index.as_view(), name='landing'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('settings/', settings.as_view(), name='settings'),
    path('search/', views.UserSearch, name='search'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    path('like/<int:pk>/', AddLike.as_view(), name='like'),
    path('foryou/', FollowingPage.as_view(), name='foryoupage'),
    path('comment/<int:pk>/', CommentPage.as_view(), name='comment'),
    path('comment/<int:pk>/like/', AddCommentLike.as_view(), name='comment-like'),
]