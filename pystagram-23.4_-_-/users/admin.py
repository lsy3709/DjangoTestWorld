from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


class FollowersInline(admin.TabularInline):
    model = User.following.through
    fk_name = "from_user"
    verbose_name = "내가 팔로우 하고 있는 사용자"
    verbose_name_plural = f"{verbose_name} 목록"


class FollowingInline(admin.TabularInline):
    model = User.following.through
    fk_name = "to_user"
    verbose_name = "나를 팔로우 하고 있는 사용자"
    verbose_name_plural = f"{verbose_name} 목록"


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ("username", "password"),
            },
        ),
        ("개인정보", {"fields": ("first_name", "last_name", "email")}),
        (
            "추가필드",
            {
                "fields": ("profile_image", "short_description"),
            },
        ),
        (
            "연관객체",
            {
                "fields": ("like_posts",),
            },
        ),
        (
            "권한",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (
            "중요한 일정",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    ]
    inlines = [
        FollowersInline,
        FollowingInline,
    ]
