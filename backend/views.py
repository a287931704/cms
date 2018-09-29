from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello(request):
    return HttpResponse('Hello World')


def helloworld(request):
    content = {}
    content['hello'] = 'hello world!!'
    content['myworld'] = 'my world!!!'
    return render(request, 'web_index.html', content)


def testsearch(request):
    return render(request, 'web_search.html')


def printuser(request):
    myinfo = {'user': 'aa', 'pwd': 'pwaa'}
    return render(request, 'web_base.html', myinfo)


def index(request):
    return render(request, 'web_index.html')


def index2(request):
    return render(request, 'web_index2.html')
