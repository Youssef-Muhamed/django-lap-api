from posts.models import Post


import json

from posts.api.serializers import PostSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from posts.models import Post




@csrf_exempt
def posts_api(request):
    if request.method =='GET':
        posts=Post.get_all_posts()
        serialized_posts=[]
        for post in posts:
            serialized_posts.append(PostSerializer(post).data)
        return JsonResponse(serialized_posts,safe=False)

    elif request.method=='POST':
        post_data=json.loads(request.body)
        post = Post.objects.create(**post_data)
        return JsonResponse(PostSerializer(post).data)


@csrf_exempt
def post_api(request,id):
    post=Post.get_post(id)
    if request.method=='GET':

        return JsonResponse(PostSerializer(post).data)
    elif request.method=='PUT':
        update_data=json.loads(request.body)
        post.title=update_data['title']
        post.description=update_data['description']
        post.save()
        return JsonResponse(PostSerializer(post).data)
    elif request.method=='DELETE':
        post.delete()
        return JsonResponse({'Post deleted':1})