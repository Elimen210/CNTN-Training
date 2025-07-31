from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from .models import Post, Comment
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import PostForm, CommentForm

class index(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()

        for post in posts:
            if post.video:
                ext = post.video.url.lower()
                post.is_video = ext.endswith('.mp4')
                post.is_audio = ext.endswith('.mp3')
            else:
                post.is_video = False
                post.is_audio = False

        context = {
                'post_list': posts,
                'form': form,
            }

        return render(request, 'landing/index.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST, request.FILES)

        for post in posts:
            if post.video:
                ext = post.video.url.lower()
                post.is_video = ext.endswith('.mp4')
                post.is_audio = ext.endswith('.mp3')
            else:
                post.is_video = False
                post.is_audio = False

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            context = {
                'post_list': posts,
                'form': form,
            }

            return HttpResponseRedirect(request.path)

        return render(request, 'landing/index.html', context)

class settings(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/settings.html')

class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile_user = profile.user
        posts = Post.objects.filter(author=profile_user).order_by('created_on')
        current_user_profile = request.user.profile
        form = PostForm()

        followers = profile.followers.all()

        number_of_followers = profile.number_of_followers
        number_of_following = profile.number_of_following

        is_following = request.user in followers.all()


        context = {
            'profile': profile,
            'profile_user': profile_user,
            'posts': posts,
            'form': form,
            'number_of_followers': number_of_followers,
            'number_of_following': number_of_following,
            'is_following': is_following,
        }

        return render(request, 'landing/profile.html', context)

    def post(self, request, pk, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
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

class CommentPage(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post).order_by('created_on')
        form = CommentForm()

        context = {
                'post': post,
                'form': form,
                'comments': comments,
                'autoplay': True
            }

        return render(request, 'landing/comment.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post).order_by('created_on')
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            return redirect(request.path)

        context = {
                'post': post,
                'form': form,
                'comments': comments,
            }

        return render(request, 'landing/comment.html', context)

class FollowingPage(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        current_user_profile = request.user.profile
        following_users = current_user_profile.following.all()  

        posts = Post.objects.filter(author__in=following_users).order_by('-created_on')
        form = PostForm()

        context = {
                'post_list': posts,
                'form': form,
            }

        return render(request, 'landing/following.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)
        
        context = {
                'post_list': posts,
                'form': form,
            }

        return render(request, 'landing/following.html', context)


def UserSearch(request):
    query = request.GET.get('query')
    profile_list = UserProfile.objects.filter(
        Q(user__username__icontains=query)
    )

    context = {
            'profile_list': profile_list,
        }

    return render(request, 'landing/search.html', context)

class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.add(request.user)

        current_user_profile = request.user.profile
        current_user_profile.following.add(profile.user)

        return redirect('profile', pk=profile.pk)


class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.remove(request.user)

        current_user_profile = request.user.profile
        current_user_profile.following.remove(profile.user)

        return redirect('profile', pk=profile.pk)

class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_like = False

        is_like = request.user in post.likes.all()

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

