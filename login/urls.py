from django.urls import path
from . import views
from .views import index, loginView, signupView, logout_view

urlpatterns = [
    path('signin/', views.loginView, name='signin'),
    path('signup/', views.signupView, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('', index.as_view(), name='login-home'),
]
