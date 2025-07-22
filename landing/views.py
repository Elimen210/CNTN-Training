from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import PostForm

class index(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()

        context = {
                'post_list': posts,
                'form': form,
            }

        return render(request, 'landing/index.html', context)
        
        if not request.user.is_authenticated:
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            context = {
                'post_list': posts,
                'form': form,
            }

        return render(request, 'landing/index.html', context)

class settings(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/settings.html')
        if not request.user.is_authenticated:
                return redirect(f"{settings.LOGIN_URL}?next={request.path}")

class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile_user = profile.user
        posts = Post.objects.filter(author=profile_user).order_by('created_on')
        form = PostForm()

        context = {
            'profile': profile,
            'profile_user': profile_user,
            'posts': posts,
            'form': form,
        }

        return render(request, 'landing/profile.html', context)
        if not request.user.is_authenticated:
                return redirect(f"{settings.LOGIN_URL}?next={request.path}")

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            context = {
                'posts': posts,
                'form': form,
            }

        return render(request, 'landing/index.html', context)
        if not request.user.is_authenticated:
                return redirect(f"{settings.LOGIN_URL}?next={request.path}")
