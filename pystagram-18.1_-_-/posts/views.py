from django.http import (
    HttpResponseBadRequest,
    HttpResponseRedirect,
    HttpResponseForbidden,
)
from django.shortcuts import render, redirect

from posts.forms import CommentForm
from posts.models import Post, Comment


def feeds(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("/users/login/")

    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        "posts": posts,
        "comment_form": comment_form,
    }
    return render(request, "posts/feeds.html", context)


# 댓글 작성을 처리할 View
def comment_add(request):
    if request.method == "GET":
        # 이 View에 GET요청이 전달되면, 잘못된 요청임을 브라우저에 알려준다.
        return HttpResponseBadRequest()

    # request.POST로 전달된 데이터를 사용해 CommentForm인스턴스를 생성
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # commit=False옵션으로 메모리상에 Comment객체 생성
        comment = form.save(commit=False)

        # Comment생성에 필요한 사용자정보를 request에서 가져와 할당
        comment.user = request.user

        # DB에 Comment객체 저장
        comment.save()

        # 생성된 Comment의 정보 확인
        print(comment.id)
        print(comment.content)
        print(comment.user)

        # 생성한 comment에서 연결된 post정보를 가져와서 id값을 사용
        return HttpResponseRedirect(f"/posts/feeds/#post-{comment.post.id}")


def comment_delete(request, comment_id):
    if request.method == "POST":
        comment = Comment.objects.get(id=comment_id)
        if comment.user == request.user:
            comment.delete()
            return HttpResponseRedirect(f"/posts/feeds/#post-{comment.post.id}")
        else:
            return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다")
    else:
        # 이 View에 오는 GET요청은 잘못되었다고 브라우저에 돌려준다
        return HttpResponseBadRequest()
