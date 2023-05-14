from django import template
from core.models import User, Profile


register = template.Library()


@register.simple_tag()
def getprofile(post):
    user = User.objects.get(username=post.user)
    profile = Profile.objects.get(user=user)
    return profile.profileImg.url


