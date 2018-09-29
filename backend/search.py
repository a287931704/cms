# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.handlers.wsgi import WSGIRequest


# 表单
def search_form(request):
    return render_to_response("web_search.html")


def base(request):
    return render(request, "web_base.html")


# 接受请求数据
def search(request):
    request.encoding = 'utf-8'
    request1 = request  # type: WSGIRequest
    if 'q' in request.GET:
        message = request.GET['q'].encode('utf-8')
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
