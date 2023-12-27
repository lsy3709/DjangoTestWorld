from django.shortcuts import render, redirect


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/posts/feeds/")
    return render(request, "users/login.html")
