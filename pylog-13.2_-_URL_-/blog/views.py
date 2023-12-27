from django.shortcuts import render

from blog.models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "post_list.html", context)


def post_detail(request, post_id):
    return render(request, "post_detail.html")
