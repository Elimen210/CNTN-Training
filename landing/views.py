from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile

class index(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')

        context = {
                'post_list': posts,
            }

        return render(request, 'landing/index.html', context)
        
        if not request.user.is_authenticated:
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")

class profile(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/profile.html')
        if not request.user.is_authenticated:
                return redirect(f"{settings.LOGIN_URL}?next={request.path}")

class settings(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/settings.html')
        if not request.user.is_authenticated:
                return redirect(f"{settings.LOGIN_URL}?next={request.path}")

class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('created_on')

        context = {
            'profile': profile,
            'user': user,
            'posts': posts,
        }

        return render(request, 'landing/profile.html', context)

    