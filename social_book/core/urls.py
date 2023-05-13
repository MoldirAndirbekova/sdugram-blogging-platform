from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<uuid:id>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post_detail/<uuid:id>/', views.post_detail, name='post_detail'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('settings', views.settings, name='settings'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('like_post', views.like_post, name='like_post'),
    path('search', views.search, name='search'),
]
