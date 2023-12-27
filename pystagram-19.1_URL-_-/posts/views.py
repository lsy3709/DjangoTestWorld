from django.http import (
    HttpResponseBadRequest,
    HttpResponseRedirect,
    HttpResponseForbidden,
)
from django.shortcuts import render, redirect

from posts.forms import CommentForm, PostForm
from posts.models import Post, Comment, PostImage


def feeds(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("/users/login2/")

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


def post_add(request):
    if request.method == "POST":
        # request.POST로 온 데이터 ("content")는 PostForm으로 처리
        form = PostForm(request.POST)

        if form.is_valid():
            # Post의 "user"값은 request에서 가져와 자동할당한다
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            # Post를 생성 한 후
            # request.FILES.getlist("images")로 전송된 이미지들을 순회하며 PostImage객체를 생성한다
            for image_file in request.FILES.getlist("images"):
                # request.FILES또는 request.FILES.getlist()로 가져온 파일은
                # Model의 ImageField부분에 곧바로 할당한다
                PostImage.objects.create(
                    post=post,
                    photo=image_file,
                )

            # 모든 PostImage와 Post의 생성이 완료되면
            # 피드페이지로 이동하여 생성된 Post의 위치로 스크롤되도록 한다
            url = f"/posts/feeds/#post-{post.id}"
            return HttpResponseRedirect(url)

    # GET요청일 때는 빈 form을 보여주도록한다
    else:
        form = PostForm()

    context = {"form": form}
    return render(request, "posts/post_add.html", context)
