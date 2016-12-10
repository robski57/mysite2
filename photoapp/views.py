from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .wikipediaApi import summary
from .twitterApi import searchTwitter

class HomeView(TemplateView):
    template_name = 'home.html'

def index(request):
    return render(request, 'photoapp/home.html')

def contact(request):
    return render(request, 'photoapp/basic.html',{'content':['If you would like to contact me, please email me','robski577@gmail.com']})

def search(request):
    return render(request, 'header.html')

def tweetArticle(request):
    query = request.GET.get('search')
    if query:
        sums = searchTwitter(query)

    return render(request, 'photoapp/Post.html', {'sums': sums})

def summaryArticle(request):
    query = request.GET.get('search')
    if query:
        sum = searchTwitter(query)


    return render(request, 'photoapp/Post.html', {'sum': sum})
