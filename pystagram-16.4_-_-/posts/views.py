from django.shortcuts import render, redirect


def feeds(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("/users/login/")
    return render(request, "posts/feeds.html")
