#coding:utf-8
from django.http import HttpResponse
# HttpResponse是django封装好的一个响应方式
from django.template.loader import get_template   #加载模板的方法
from django.template import Context               #进行数据的传输
from django.shortcuts import render_to_response   #一个快读的响应方式，

class hero():
    def __init__(self):
        self.HP=100
        self.MP=100
    def fight(self):
        self.HP-=10
def fun(request):
    # name="foraa"
    # age=18
    return render_to_response("index.html",locals())

# def fun2(request):
#     # name="for"
#     # age=18
#     # name2="while"
#     # con = hero()
#     # content = {"name": "while", "age": 18}
#     # testList=['a','b','c']
#     return render_to_response("index.html",locals())