from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    user_picture = models.ImageField(upload_to='uploads/userprofile', default='uploads/userprofile/default.jpeg', blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    followers = models.ManyToManyField(User, related_name='followers', blank=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)

    @property
    def number_of_followers(self):
        return self.followers.count()

    @property
    def number_of_following(self):
        return UserProfile.objects.filter(followers=self.user).count()