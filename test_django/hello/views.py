from django.shortcuts import render
from django.http import HttpResponse, FileResponse


# Create your views here.
def hello_world(request):
    return HttpResponse('hello world')

def article_list(request, month):
    return HttpResponse('article:{}'.format(month))

def is_odd(request, num):
    if num < 1 or num > 100:
        print('输入的数字不符合要求（要求1-100之间）')
    else:
        if num % 2 == 0:
            return HttpResponse('{}是偶数'.format(num))
        else:
            return HttpResponse('{}是奇数'.format(num))

def http_req(request):
    print(request.method)
    print(request.headers)
    print(request.headers['user-agent'])

    print(request.META.get('User-Agent'))
    return HttpResponse('响应')

