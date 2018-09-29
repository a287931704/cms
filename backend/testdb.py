# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from first_test.models import Test


# 数据库操作
def testdb(request):
    # test1 = Test(name='w3cschool.cn')
    # test1.save()
    tmplist = []
    list = Test.objects.all()
    for var in list:
        Test.objects.filter(id=var.id).update(name="%s-%s" % (var.name[:10], var.id))
        newlist = Test.objects.filter(id=var.id)
        for var1 in newlist:
            mapinfo = {"id": var1.id, "name": var1.name}
            tmplist.append(mapinfo)
    return render(request, "web_base.html", {"data": tmplist})
    # return HttpResponse("<p>数据添加成功！</p>")
