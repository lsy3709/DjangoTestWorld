from django.shortcuts import redirect


def index(request):
    if request.user.is_authenticated:
        return redirect("posts:feeds")
    else:
        return redirect("users:login")
