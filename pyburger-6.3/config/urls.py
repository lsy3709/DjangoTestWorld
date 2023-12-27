from django.contrib import admin
from django.urls import path

from config.views import main, burger_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main),
    path("burgers/", burger_list),
]
