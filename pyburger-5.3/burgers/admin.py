from django.contrib import admin

from burgers.models import Burger


@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    pass
