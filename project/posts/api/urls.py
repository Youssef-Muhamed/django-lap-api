from django.urls import path ,include
from posts.api.views import post_api, posts_api 



urlpatterns = [
    path('',posts_api,name='api.posts'),
    path('<int:id>',post_api,name='api.post'),
]
