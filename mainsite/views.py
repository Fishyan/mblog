from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    # posts = Post.title.all()

    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("No. {}:".format(str(count))+str(post)+"<br>")
    return HttpResponse(post_lists)
