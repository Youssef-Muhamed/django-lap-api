from django.urls import path ,include



urlpatterns = [
    # path('',),
    path('api/',include('posts.api.urls')),
]
