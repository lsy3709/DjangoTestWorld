from django.contrib import admin
from django.urls import path

from config.views import main, burger_list, burger_search

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main),
    path("burgers/", burger_list),
    path("search/", burger_search),
]
