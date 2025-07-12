from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Post

class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')

class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')

        context = {
                'post_list': posts,
            }

        return render(request, 'landing/index.html', context)