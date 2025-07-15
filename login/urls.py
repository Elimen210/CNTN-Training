from django.urls import path
from . import views
from .views import index, loginView, signupView

urlpatterns = [
    path('signin/', views.loginView, name='signin'),
    path('signup/', views.signupView, name='signup'),
    path('', index.as_view(), name='index'),
]
