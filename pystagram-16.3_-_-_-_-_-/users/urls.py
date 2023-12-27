from django.urls import path

from users.views import login_view

urlpatterns = [
    path("login/", login_view),
]
