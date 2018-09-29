from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import UserInfo


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

def check_register(request):
    if request.is_ajax():
        username=request.POST['username']
        t_userinfo = UserInfo.objects.get()

@ensure_csrf_cookie
def register(request):
    ctx = {}
    ctx.update(csrf(request))
    if request.POST:
        ctx['username'] = request.POST['Name']
        ctx['email'] = request.POST['Email']
        ctx['password'] = request.POST['Password']
        ctx['phone'] = request.POST['Phone Number']
        t_userinfo = UserInfo(username=ctx['username'], password=ctx['password'], email=ctx['email'], phone=ctx['phone'])
        t_userinfo.save()
        return render(request, 'web_search.html', ctx)


@ensure_csrf_cookie
def login(request):
    ctx = {}
    ctx.update(csrf(request))
    render(request, 'web_base.html')
