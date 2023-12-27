from django.shortcuts import render, redirect

from posts.models import Post


def feeds(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("/users/login/")

    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "posts/feeds.html", context)
