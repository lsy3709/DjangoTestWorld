import admin_thumbnails
from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple
from django.utils.safestring import mark_safe

from posts.models import Post, PostImage, Comment, HashTag


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class InlineImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        if value and getattr(value, "url", None):
            html = mark_safe(f'<img src="{value.url}" width="150" height="150">') + html
        return html


@admin_thumbnails.thumbnail("photo")
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


class LikeUserInline(admin.TabularInline):
    model = Post.like_users.through
    verbose_name = "좋아요 한 User"
    verbose_name_plural = f"{verbose_name} 목록"
    extra = 1

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "content",
        "created",
    ]
    inlines = [
        CommentInline,
        PostImageInline,
        LikeUserInline,
    ]
    formfield_overrides = {ManyToManyField: {"widget": CheckboxSelectMultiple}}


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "photo",
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "content",
        "created",
    ]


@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    pass
