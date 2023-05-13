from django.contrib import admin
<<<<<<< HEAD
from .models import Profile, Post, LikePost, Comment
from . import models


=======
from .models import Profile, Post, LikePost, FollowersCount
>>>>>>> fdcc84518bdce3992d821f2148e460957a557586
# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
<<<<<<< HEAD
admin.site.register(Comment)
=======
admin.site.register(FollowersCount)
>>>>>>> fdcc84518bdce3992d821f2148e460957a557586
