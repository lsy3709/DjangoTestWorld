from django.urls import path

from users.views import login_view, logout_view, signup, profile, followers, following

app_name = "users"
urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup, name="signup"),
    path("<int:user_id>/profile/", profile, name="profile"),
    path("<int:user_id>/followers/", followers, name="followers"),
    path("<int:user_id>/following/", following, name="following"),
]
