from django.shortcuts import render


def feeds(request):
    return render(request, "posts/feeds.html")
