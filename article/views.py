from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render(request,'home.html',{'post_list':post_list})
    # return HttpResponse("Hello World,Django")

def detail(request,id):

    post = Article.objects.all()[int(id)]
    str = ("title = %s,category = %s, date_time = %s, content = %s" %(post.title,post.category,post.date_time,post.content))
    return HttpResponse(str)
    # return HttpResponse("You are looking at my_args %s." %my_args)

def test(request):
    return render(request,'test.html',{'current_time':datetime.now()})