from django.contrib import admin
from . import models
from .models import Profile, Post, LikePost, FollowersCount,Comment

# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(Comment)
admin.site.register(FollowersCount)

