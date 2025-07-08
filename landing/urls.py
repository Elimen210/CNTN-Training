from django.urls import include, re_path
import HelloDjangoApp.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    re_path(r'^$', HelloDjangoApp.views.index, name='index'),
    re_path(r'^home$', HelloDjangoApp.views.index, name='home')
]
