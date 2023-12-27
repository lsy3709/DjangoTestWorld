from django.urls import path

from posts.views import feeds, comment_add, comment_delete, post_add

app_name = "posts"
urlpatterns = [
    path("feeds/", feeds, name="feeds"),
    path("comment_add/", comment_add, name="comment_add"),
    path("comments/<int:comment_id>/delete/", comment_delete, name="comment_delete"),
    path("post_add/", post_add, name="post_add"),
]
