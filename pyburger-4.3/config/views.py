from django.http import HttpResponse


def main(request):
    return HttpResponse("안녕하세요, pyburger입니다")


def burger_list(request):
    return HttpResponse("pyburger의 햄버거 목록입니다")
